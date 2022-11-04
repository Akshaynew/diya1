from django.shortcuts import render
from django.http import HttpResponse
from.models import items
# Create your views here.
def index(request):
    products=items.objects.all()
    return render(request,'list.html',{'items':products})
    #return HttpResponse("<h1>Welcome to django</h1>")