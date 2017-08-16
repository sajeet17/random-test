import random
from django.http import HttpResponse
from django.shortcuts import render


# function based views
def home(request):
    num = random.randint(0, 9)
    foo = [True, False]
    luck = random.choice(foo)
    lucky_elements = ["fire", "water", "earth", "wind", "metal"]

    context = {"html_var": luck,
               "num": num,
               "lucky_element": random.choice(lucky_elements)}
    return render(request, "base.html", context)


'''
def home(request):
    return render(request,"template",{"html_var":"context variable"})
'''
