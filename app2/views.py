from django.shortcuts import redirect, render
from app2.models import data

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def signup(request):
    return render(request, 'signup.html')

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
    data_list = data.objects.all()
    return render(request,'admin.html',{'data_list':data_list})