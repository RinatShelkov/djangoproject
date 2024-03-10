# Create your views here.
from django.shortcuts import render


def conacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
