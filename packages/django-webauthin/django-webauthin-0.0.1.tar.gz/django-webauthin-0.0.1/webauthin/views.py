import base64
import random
import string

import webauthn
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import AuthData

ICON = "https://example.com/"

User = get_user_model()


def get_challenge() -> str:
    return "".join(
        [
            random.SystemRandom().choice(string.ascii_letters + string.digits)
            for i in range(32)
        ]
    )


def login_view(request):
    return render(request, "webauthin_login.html")


@csrf_exempt
@login_required
def register_begin(request):
    site = get_current_site(request)
    challenge = get_challenge()
    request.session["challenge"] = challenge
    reg_data = webauthn.WebAuthnMakeCredentialOptions(
        challenge=challenge,
        rp_name=site.name,
        rp_id=site.domain,
        user_id=base64.b64encode(str(request.user.id).encode()).decode(),
        username=request.user.get_username(),
        display_name="%s user: %s" % (site.name, request.user.get_username()),
        icon_url=ICON,
        attestation="none",
        user_verification="required",
    ).registration_dict
    # This is needed so the key gets stored on the authenticator, I think.
    reg_data["authenticatorSelection"]["requireResidentKey"] = True
    return JsonResponse(reg_data)


@csrf_exempt
@login_required
def register_verify(request):
    site = get_current_site(request)
    challenge = request.session.get("challenge")
    if not challenge:
        return JsonResponse("No challenge exists in your session.", status=422)

    registration_response = request.POST
    webauthn_registration_response = webauthn.WebAuthnRegistrationResponse(
        rp_id=site.domain,
        origin="https://%s" % site.domain,
        registration_response=registration_response,
        challenge=challenge,
        self_attestation_permitted=True,
        none_attestation_permitted=True,
        uv_required=True,
    )

    try:
        webauthn_credential = webauthn_registration_response.verify()
    except Exception as e:
        messages.error(request, "Registration failed. Error: {}".format(e))
        return JsonResponse({"fail": "Registration failed. Error: {}".format(e)})

    auth_data = AuthData.objects.filter(credential_id=webauthn_credential.credential_id)
    if auth_data.exists():
        messages.error(
            request,
            "This key is already registered to an account. Try logging in with it.",
        )
        return JsonResponse({"fail": "Credential ID already exists."}, status=422)

    webauthn_credential.credential_id = str(webauthn_credential.credential_id, "utf-8")
    webauthn_credential.public_key = str(webauthn_credential.public_key, "utf-8")
    AuthData.objects.create(
        user=request.user,
        credential_id=webauthn_credential.credential_id,
        public_key=webauthn_credential.public_key,
    )
    messages.success(request, "Your key has been successfully registered.")
    return JsonResponse({"success": "User successfully registered."})


@csrf_exempt
def login_begin(request):
    site = get_current_site(request)
    challenge = get_challenge()
    request.session["challenge"] = challenge
    login_data = {
        "challenge": request.session["challenge"],
        "timeout": 60000,
        "rpId": site.domain,
        "allowCredentials": [],
        "userVerification": "required",
        "extensions": {
            "txAuthSimple": "FIDO",
            "txAuthGenericArg": {"contentType": "text/plain", "content": "RklETw=="},
            "uvi": True,
        },
        "status": "ok",
        "errorMessage": "Error while logging in.",
    }

    return JsonResponse(login_data)


@csrf_exempt
def login_verify(request):
    challenge = request.session.get("challenge")
    if not challenge:
        return JsonResponse("No challenge exists in your session.", status=422)

    print(request.POST)

    user = authenticate(request, credential_id=request.POST["id"], data=request.POST)
    if user is None:
        return JsonResponse({"fail": "Assertion failed."}, status=422)

    login(request, user)

    return JsonResponse({"success": True})
