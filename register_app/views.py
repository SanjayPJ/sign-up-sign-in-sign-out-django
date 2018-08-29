from django.shortcuts import render
from register_app.forms import UserForm

# Create your views here.

def register(request):
    is_registered = False

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user_form = form.save()
            user_form.set_password(user_form.password)
            user_form.save()
            form = UserForm()

            is_registered = True
        else:
            print(form.errors)
    else:
        form = UserForm()

    return render(request, "register.html", {
        "form" : form,
        "is_registered" : is_registered
    })