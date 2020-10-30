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
        form = FeebackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydictionary = {
                "form":FeebackForm()
            }
            errorFlag=False;
            Errors = []
            if title != title.upper():
                errorFlag = True
                errormsg = "Title should be capital"
                Errors.append(errormsg)

            import re
            regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
            if not re.search(regex,email):
                errorFlag=True
                errormsg="Not a valid email"
                Errors.append(errormsg)
            if errorFlag!=True:

                mydictionary["success"]=True
                mydictionary["successmsg"]="Form Submitterd"
            
            mydictionary["error"]=errorFlag
            mydictionary["errors"]=Errors
            return render(request,'myform2.html',context=mydictionary)
        else:
            mydictionary={
                "form":form
            }
            return render(request,'myform2.html',context=mydictionary)

    elif request.method == "GET":
        form = FeebackForm()
        mydictionary={
            "form":form
        }
        return render(request,'myform2.html',context=mydictionary)

def error_404_view(request,exception):
    return render(request,'404.html')