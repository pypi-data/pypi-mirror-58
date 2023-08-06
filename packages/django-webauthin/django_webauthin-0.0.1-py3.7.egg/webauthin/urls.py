from django.urls import path

from . import views


app_name = "webauthin"
urlpatterns = [
    path(r"login/begin/", views.login_begin, name="login-begin"),
    path(r"login/verify/", views.login_verify, name="login-verify"),
    path(r"register/begin/", views.register_begin, name="register-begin"),
    path(r"register/verify/", views.register_verify, name="register-verify"),
    path(r"login/", views.login_view, name="login"),
]
