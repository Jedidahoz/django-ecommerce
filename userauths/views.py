from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully")

            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            
            login(request, new_user)
            return redirect('userauths:login')

    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('base:home')

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request, f"User with {email} does not exist.")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")

            return redirect('base:home')
        else:
            messages.warning(request, "User does not exits, Create an account.")

    context = {}

    return render(request, "auth/login.html", context)

def user_logout(request):
    logout(request)
    messages.success(request, "You're logged out")
    return redirect("userauths:login")