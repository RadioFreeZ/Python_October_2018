from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

from random import *
import string

def index(request):
    return render(request,'index.html')
def random(request):
    if request.method == "POST":
        context = {
            "word" : get_random_string(length=14)
        }
        request.session["word"] = context["word"]
        return redirect("/")
    else:
        return redirect("/")
def reset(request):
    request.session.clear()
    return redirect("/")
