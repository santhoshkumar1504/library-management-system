import requests 
from django.shortcuts import render, redirect
from .forms import *


def register(request):
    message = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            response = requests.post(
                "http://127.0.0.1:8000/api/register/",
                json=form.cleaned_data
            )
            return redirect('login')
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        try:
            data = response.json()
            message = data.get("message", data)
        except Exception:
                message = response.text

    else:
        form = RegisterForm()

    return render(request, "register.html", {
        "form": form,
        "message": message
    })



def login(request):
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            response = requests.post(
                "http://127.0.0.1:8000/api/login/",
                json=form.cleaned_data
            )

            if response.status_code == 200:
                data = response.json()

                # Store JWT tokens in session
                request.session["access"] = data.get("access")
                request.session["refresh"] = data.get("refresh")

                return redirect("profile")

            print("Status Code:", response.status_code)
            print("Response Text:", response.text)

            try:
                data = response.json()
                message = data.get("message", data)
            except Exception:
                message = response.text

    else:
        form = LoginForm()

    return render(request, "login.html", {
        "form": form,
        "message": message
    })

def profile(request):
    access = request.session.get("access")
    response = requests.get(
        "http://127.0.0.1:8000/api/profile/",
        headers={
            "Authorization": f"Bearer {access}"
        }
    )
    data = {}
    if response.status_code == 200:
        data = response.json()

    return render(request, "profile.html", {
        "profile": data
    })



def update(request):

    message = ""

    access = request.session.get("access")

    headers = {
        "Authorization": f"Bearer {access}"
    }

    # ---------------- UPDATE ----------------

    if request.method == "POST":

        form = UpdateProfileForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            data = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email"],
                "phone": form.cleaned_data["phone"],
                "address": form.cleaned_data["address"],
                "city": form.cleaned_data["city"],
                "state": form.cleaned_data["state"],
                "pincode": form.cleaned_data["pincode"],
            }

            files = {}

            if "profile_image" in request.FILES:
                files["profile_image"] = request.FILES["profile_image"]

            response = requests.put(
                "http://127.0.0.1:8000/api/update-profile/",
                data=data,
                files=files,
                headers=headers
            )

            try:
                result = response.json()
                message = result.get("message", result)

            except Exception:
                message = response.text

    # ---------------- GET PROFILE ----------------

    response = requests.get(
        "http://127.0.0.1:8000/api/profile/",
        headers=headers
    )

    profile = {}

    if response.status_code == 200:

        profile = response.json()

        form = UpdateProfileForm(initial={

            "first_name": profile.get("first_name"),

            "last_name": profile.get("last_name"),

            "email": profile.get("email"),

            "phone": profile.get("phone"),

            "address": profile.get("address"),

            "city": profile.get("city"),

            "state": profile.get("state"),

            "pincode": profile.get("pincode"),

        })
    else:
        form=UpdateProfileForm()

    return render(
        request,
        "update.html",
        {
            "form": form,
            "profile": profile,
            "message": message
        }
    )


def change_password(request):

    message = ""

    access = request.session.get("access")

    if request.method == "POST":

        form = ChangePasswordForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            response = requests.post(
                "http://127.0.0.1:8000/api/change-password/",
                json=form.cleaned_data,
                headers={
                    "Authorization": f"Bearer {access}"
                }
            )

            try:
                data = response.json()

                if "message" in data:
                    message = data["message"]
                elif "error" in data:
                    message = data["error"]
                else:
                    message = data

            except Exception:
                message = response.text

    else:
        form = ChangePasswordForm()

    return render(request, "change_password.html", {
        "form": form,
        "message": message
    })

def forgot_password(request):
    message = ""
    show_reset = False

    if request.method == "POST":

        form = ForgotPasswordForm(request.POST)

        if form.is_valid():

            response = requests.post(
                "http://127.0.0.1:8000/api/forgot-password/",
                json=form.cleaned_data
            )

            try:
                data = response.json()

                if "message" in data:
                    message = data["message"]
                    show_reset = True

                    # Save email so it can be used later
                    request.session["reset_email"] = form.cleaned_data["email"]

                else:
                    message = data["error"]
                    show_reset = False

            except:
                message = response.text
                show_reset = False

    else:
        form = ForgotPasswordForm()

    return render(request, "forgot_password.html", {
        "form": form,
        "message": message,
        "show_reset": show_reset,
    })


def reset_password(request):
    message = ""

    if request.method == "POST":
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            response = requests.post(
                "http://127.0.0.1:8000/api/reset-password/",
                json=form.cleaned_data
            )

            try:
                data = response.json()
                message = data.get("message", data)
                return render(request,"login.html")
            except Exception:
                message = response.text

    else:
        form = ResetPasswordForm()

    return render(request, "reset_password.html", {
        "form": form,
        "message": message
    })


def logout(request):
    request.session.flush()
    return redirect("login")