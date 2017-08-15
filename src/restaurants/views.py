import random
from django.http import HttpResponse
from django.shortcuts import render


# function based views
def home(request):
    num = random.randint(0, 9)
    foo = [True, False]
    luck = random.choice(foo)
    return render(request, "base.html", {"html_var": luck, "num": num})


'''
def home(request):
    return render(request,"template",{"html_var":"context variable"})
'''
