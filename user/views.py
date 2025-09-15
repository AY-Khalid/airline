from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "user/index.html", {
        "user": request.user
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # ✅ pass request AND user
            return redirect(reverse("index"))
        else:
            return render(
                request, "user/login.html", {"message": "Invalid username or password."}
            )
    return render(request, "user/login.html")


def logout_view(request):
    logout(request)  # logs out the user
    messages.success(request, "You are logged out.")  # add flash message
    return redirect(reverse("login"))
