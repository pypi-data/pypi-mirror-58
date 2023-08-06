WebAuthin'
==========

WARNING: This library is still somewhat of an alpha version, though it should mostly work.


About
-----

WebAuthin' is a Django library for secure, passwordless logins using WebAuthn/FIDO2.

It allows users to associate secure keys (from USB keys like Yubikeys, Titan keys, etc
to platform authenticators like OS X's TouchID) with your website and log in just by
plugging the key in. This means they don't need to remember a username/password, there
are no credentials to steal, and they don't need a second factor.

WebAuthin' requires user verification, which means that the user will need to enter a
PIN, fingerprint, or some other method of verification locally, to prevent theft of the
physical key from allowing logins.

WebAuthn is currently only supported on a few browsers (Chrome on the desktop, somewhat
on Firefox on Android, possibly Safari on iOS).


[![PyPI version](https://img.shields.io/pypi/v/django-webauthin.svg)](https://pypi.python.org/pypi/django-webauthin)


Installing django-webauthin
---------------------------

* First of all, make sure that your site uses the [`Sites`
  framework](https://docs.djangoproject.com/en/3.0/ref/contrib/sites/) properly, as that
  is what WebAuthin' currently uses to get your site name and domain. In the future,
  settings will be added so you won't need to do this.

* Install django-webauthin using pip: `pip install django-webauthin`

* Add `webauthin` to your `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = [... "webauthin", ...]
```

* Add webauthin to your authentication backends:

```python
AUTHENTICATION_BACKENDS = (
    "webauthin.auth_backends.WebAuthinBackend",
    "django.contrib.auth.backends.ModelBackend",
)
```

* Add the webauthin URL to your `urls.py`:

```python
# urls.py
urlpatterns += path("auth/", include("webauthin.urls", namespace="webauthin"))
```

* You now need two buttons, one for registration and one for login. The registration
  button should have an ID of `webauthin-register`. You also need to include a
  template that will insert the JS code somewhere:

```html
{% include "webauthin_register.html" %}
<button id="webauthin-register">Register new key</button>
```

Pressing this button will trigger the key registration flow.


* Add the login button to your login form, as above, this time with an ID of
  `webauthin-login`:

```html
{% include "webauthin_login.html" %}
<button id="webauthin-login">Log in using hardware key</button>
```

* You can also add a table to allow the user to see and delete their registered keys,
  though this process is currently somewhat manual:

```html
{% for key in request.user.authdata_set.all %}
<p>
    {{ key.name }}: Created on {{ key.created_on }} and last used on
    {{ key.last_used_on }}.

    <form
        method="POST"
        action="{% url "webauthin:delete-key" %}"
        onsubmit="return confirm('Are you sure you want to delete this key?');"
    >{% csrf_token %}
        <input type="hidden" name="key_id" value="{{ key.id }}" />
        <button type="submit">Delete</button>
    </form>
</p>
{% endfor %}
```

You can similarly change the key name by POSTing to `webauthin:rename-key` with a
parameter called `name`.

Do note that you need to have the Django messages framework installed so the library
can show the user error/success messages.


Settings
--------

Here are the settings you can change in your `settings.py`:

* `WEBAUTHIN_LOGIN_REDIRECT_URL` (default: LOGIN_REDIRECT_URL): Where to redirect after
  a successful login.
* `WEBAUTHIN_LOGIN_ERROR_URL` (default: LOGIN_URL): Where to redirect after a login
  error.
* `WEBAUTHIN_REGISTRATION_REDIRECT_URL` (default: LOGIN_REDIRECT_URL): Where to
  redirect after a successful key registration.
* `WEBAUTHIN_REGISTRATION_ERROR_URL` (default: LOGIN_REDIRECT_URL): Where to redirect
  after a key registration error.
