from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "accounts/dashboard.html")

def products(request):
    return render(request, "accounts/products.html")

def customer(request):
    return render(request, "accounts/customer.html")



'''
-- accounts
---- templates
------ accounts
--------- dahsboard.html
--------- profile.html
--------- customer.html
'''
