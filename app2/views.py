from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from app2.models import data

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                # Create a new user with hashed password
                User.objects.create_user(username=email, email=email, password=password)
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Error: {e}')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home if login is successful
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        new_data = data(name=name, email=email, phone=phone, message=message)
        new_data.save()

        return redirect('home')
    return render(request, 'contact.html')

def admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data_list = data.objects.all()
    return render(request, 'admin.html', {'data_list': data_list})
