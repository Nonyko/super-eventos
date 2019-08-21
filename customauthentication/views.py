from django.shortcuts import render, redirect
# Create your views here.


from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .admin import UserCreationForm
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)

        else:

            messages.error(request, 'O email de usuário e senha inserida não coincidem.')
            return render(request, 'registration/login.html', {'forms': form})

    else:

        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'forms': form})


def logout_user(request):
    logout(request)

    return redirect('autenticacao:login')


def register_user(request):

    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('autenticacao:thanks')
        else:
            username = request.POST['username']
            email = request.POST['email']
            return render(request, 'registration/register.html', {'form': f, 'username': username, 'email': email})
    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})

def thanks(request):
    return render(request, 'registration/thanks.html')
