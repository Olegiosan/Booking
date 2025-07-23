from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from booking_app.views import room_list


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create_user(
                username=username,
                password=password,
            )

            login(request, user)

            return redirect('room_list')
        else:
            messages.error(request, "Введіть пароль іще раз")

    return render(
        request,
        template_name = "auth_system/register.html",
    )

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('room_list')
        else:
            messages.error(request, "Пароль або юзернейм неправильні")

    return render(
        request,
        template_name="auth_system/login.html",
    )

def logout_user(request):
    logout(request)
    return redirect('room_list')