from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms import LoginForm, SignupForm

User = get_user_model()


def signup_page(request):
    message = ""
    form = SignupForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        password2 = form.cleaned_data.get("password2")

        if password == password2:
            try:
                user = User.objects.create_user(username, email, password)
            except:
                user = None
        
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
            elif User.objects.filter(username__iexact=username).exists():
                message = "Username taken."
            else:
                message = "Signup error."
        else:
            message = "Password didn't match."
    
    context = {
        "form": form,
        "message": message,
    }
    return render(request, "accounts/signup.html", context)


def login_page(request):
    message = ""
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard:dashboard_page"))
        elif not User.objects.filter(username__iexact=username).exists():
            message = "Invalid username."
        else:
            message = "Incorrect password."

    context = {
        "form": form,
        "message": message,
    }
    return render(request, "accounts/login.html", context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login_page"))
