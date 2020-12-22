from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = "Hello World"
    greeting="hey how are you"
    fruits=['apple','mango','banana']
    num1,num2=3,5
    ans=num1>num2
    #print(ans)
    mydictionary={
        "var" : var,
        "msg" : greeting,
        "myfruits": fruits,
        "num1":num1,
        "num2":num2,

        "ans":ans
    }
    return render(request,'third.html',context=mydictionary)

def myimagepage(request):
    return render(request,'imagepage.html')

def myimagepage2(request):
    return render(request,'imagepage2.html')

def myform(request):
    return render(request,'myform.html')

def submitmyform(request):
    mydictionary={
        #var1:
        #var2:
        "method": request.method

        
    }
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            title=request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            var=str("Form Submitted "+ str(request.method))
            return HttpResponse(var)
        else:
            mydictionary={
                "form" : form
            }
            return render(request,'myform2.html',contex=mydictionary)
    elif request.method=="GET":
        form=FeedbackForm()  #FeedbackForm(none)
        mydictionary={
            "form" : form
            }
        return render(request,'myform2.html',context=mydictionary)
        

