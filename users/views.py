from django.shortcuts import render, redirect
from .forms import ContactForm, RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password == confirm_password:
                # Check if the username already exists
                if User.objects.filter(username=username).exists():
                    form.add_error('username', "Username already exists")
                else:
                    try:
                        # Create and save the user
                        user = User.objects.create_user(username=username, password=password, email=email)
                        user.save()

                        return render(request, "users/success.html", {"name": username})
                    except IntegrityError as e:
                        form.add_error(None, "Username already exists.")
            else:
                form.add_error('confirm_password', "Passwords do not match")
    else:
        form = RegistrationForm()

    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                # Invalid login
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, "users/success.html", {"name": name})
    else:
        form = ContactForm()
    
    return render(request, "users/contact.html", {"form": form})