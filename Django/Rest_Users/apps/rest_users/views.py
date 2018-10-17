from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User
def index(request):
    context = {}
    context['users'] = User.objects.all()
    return render(request,'index.html', context)
def new(request):
    return render(request,'create.html')
def create(request):
    if request.method == "POST":
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        return redirect('/users')
    else:
        return redirect('/users')
def edit(request,id):
    context = {}
    context['passed_id'] = id
    return render(request,'edit.html', context)
def update(request,id):
    user_change = User.objects.get(id = id)
    user_change.first_name = request.POST['first_name']
    user_change.last_name = request.POST['last_name']
    user_change.email = request.POST['email']
    user_change.save()
    return redirect('/users')
def delete(request,id):
    user_delete = User.objects.get(id = id)
    user_delete.delete()
    return redirect('/users')
def show(request,id):
    print(f'\nID IS:{id} \n')
    show_user = User.objects.get(id=id)
    context = {}
    context['show_user'] = show_user
    print(f'\nCONTEXT CONTAINS:{show_user} \n')
    return render(request,'show.html', context)
