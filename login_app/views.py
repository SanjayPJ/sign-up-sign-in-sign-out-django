from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_in(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                e_message = "ACCOUNT NOT ACTIVE"
                return render(request, "login.html", {
                    "e_message" : e_message
                })
        else:
            e_message = "INVALID USERNAME OR PASSWORD"
            return render(request, "login.html", {
                    "e_message" : e_message
                })
    else:
        return render(request, "login.html")

@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))