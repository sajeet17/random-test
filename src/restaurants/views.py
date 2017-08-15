import random
from django.http import HttpResponse
from django.shortcuts import render


# function based views
def home(request):
    num = random.randint(0, 9)
    return render(request, "base.html", {"html_var": " your lucky chance", "num": num})


'''
def home(request):
    return render(request,"template",{"html_var":"context variable"})
'''
