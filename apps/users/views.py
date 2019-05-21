from django.shortcuts import render
from django.shortcuts import redirect
from apps.users.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {
        "form": form
    })

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             return redirect("/")
#     else:
#         form = LoginForm()
#     return render(request, "registration/login.html", {
#         "form": form
#     })
#

@login_required
def secret_page(request):
    return render(request, 'secret_page.html', {})
