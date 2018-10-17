from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
import sys
def index(request):
    print(request, file = sys.stderr)
    response = "placeholder to display a new form to create a new blog!"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request,num):
    response = "placeholder to display blog " + num
    return HttpResponse(response)

def edit(request,num):
    response = "placeholder to edit blog " + num
    return HttpResponse(response)

def delete(request,num):
    return redirect('/')
