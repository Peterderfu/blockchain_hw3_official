from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Views here
def landing(request):
    return render(request, 'home/landing_page.html')

def index(request):
    return render(request, 'home/base_home.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def indexSipun(request):
    return render(request, 'home/base_sipun_index.html')

def registerSipun(request):
    return render(request, 'home/base_sipun_register.html')

def signupSipun(request):
    return render(request, 'home/base_sipun_signup.html')

def orderFormSipun(request):
    return render(request, 'home/base_sipun_orderForm.html')
