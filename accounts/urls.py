from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "accounts/signup/",
        views.signup_page,
        name="signup_page",
    ),
    path(
        "accounts/login/",
        views.login_page,
        name="login_page",
    ),
    path(
        "accounts/logout/",
        views.logout_page,
        name="logout_page",
    )
]