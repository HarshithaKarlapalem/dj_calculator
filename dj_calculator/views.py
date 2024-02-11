from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculator(request):
    return render(request,'calculator.html')

def calculate(request):
    # val1=request.GET["number1"]
    # val2=request.GET["number2"]
    # res=val1+val2
    if request.method=="POST":
        num1=request.POST['number1']
        num2=request.POST['number2']
        if 'add' in request.POST:
            ans=int(num1)+int(num2)
        elif 'subtract' in request.POST:
            ans=int(num1)-int(num2)
        elif 'multiply' in request.POST:
            ans=int(num1)*int(num2)
        elif 'divide' in request.POST:
            ans=int(num1)//int(num2)
    return render(request,'result.html',{"result":ans})