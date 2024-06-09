from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request,'index.html')


def check(request):
    return render(request,'calc.html')

def primecheck(request):
    return render(request,'prime.html')

def numcheck(request):
    n=request.POST['n']
    n=int(n)
    result=''
    for i in range(2,n-1):
        if n%i==0:
            result='Not Prime'
    
    if(result!='Not Prime'):
        result='Prime'
    
    return render(request,'prime.html',{'result':result})

def inbetween(request):
    n1=int(request.POST['number1'])
    n2=int(request.POST['number2'])

    result=[]
    for i in range(n1,n2):
        a=0
        for j in range(2,i):
            if i%j==0:
                a+=1
                break
        if a==0:
            result.append(i)
        n=len(result)

    return render(request,'prime.html',{'lresult':result,'size':n})


    


