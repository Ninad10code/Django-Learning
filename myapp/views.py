from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from django.template import loader
from .forms import *
# import firstDjango
import os
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World!")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name":name,
        "age":age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    # template = loader.get_template('index.html')
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    sentence = "Hello World"
    greet = "How you doing ?"
    fruits = ["apple","mango","banana"]
    num1 , num2 = 10,15
    ans = num1 > num2
    print(ans)
    mydictonary = {
        "sentence":sentence,
        "msg":greet,
        "myfruits":fruits,
        "myans":ans,
        "num1":num1,
        "num2":num2
    }
    return render(request,'third.html',context=mydictonary)

def myimagepage(request):
    return render(request,'image.html')

def myform(request):
    return render(request,'form.html')

def submitform(request):
    mydictionary = {
        "eamil":request.POST['email'],
        "password":request.POST['password'],
        "method": request.method
    }
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = FeebackForm()
        mydictionary={
            "form":form
        }
        return render(request,'myform2.html',context=mydictionary)