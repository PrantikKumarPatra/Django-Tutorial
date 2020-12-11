from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')
