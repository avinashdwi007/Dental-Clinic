from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

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
        subject = request.POST.get('subject')
        sender_email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Email details
        subject = f"Message from {sender_email}: {subject}"
        message_body = f"Message from: {sender_email}\n\nMessage:\n{message}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email_from]  # Email is sent to you
        
        try:
            send_mail(subject, message_body, email_from, recipient_list)
            
        except Exception as e:
            messages.error(request, f'Error: {e}')
            
    return render(request, 'contact.html')