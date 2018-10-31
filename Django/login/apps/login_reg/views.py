from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from django.contrib import messages
from .models import User
import datetime
from datetime import timedelta
def dash(request):
    request.session.clear()
    return render(request,'dash.html')
def register(request):
    if request.method == 'POST':
        context = {
            'first_name' : request.POST['first_name'],
            'last_name' : request.POST['last_name'],
            'email' : request.POST['email'],
            'password' : request.POST['password'],
            'password_confirm' : request.POST['password_confirm'],
            'birthday' : request.POST['birthday'],
        }

        errors = User.objects.basic_validator(request.POST)
        if not context['birthday']:
            errors["birthday"] = "Invalid Birthday"
        if context['password'] != context['password_confirm']:
            errors["password"] = "Passwords must match!"
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard/')
        hash = bcrypt.hashpw(context['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = context['first_name'], last_name = context['last_name'], email = context['email'], password = hash, birthday = context['birthday'])
        request.session['name']=context['first_name']
        messages.success(request, 'You have successfully registered!')
        return redirect('/dashboard/success')
    else:
        return redirect('/dashboard/')
def login(request):
    context = {
        'email' : request.POST['email'],
        'password' : request.POST['password']
    }
    check = User.objects.filter(email = context['email'])
    if check:
        user = User.objects.get(email = context['email'])
        if user.email:
            if bcrypt.checkpw(context['password'].encode(), user.password.encode()):
                request.session['name']=user.first_name
                messages.success(request, 'You have successfully logged in!')
                return redirect('/dashboard/success')
    errors = {}
    errors['login'] = "Login incorrect!"
    for key, value in errors.items():
        messages.error(request, value)
        return redirect('/dashboard/')
def success(request):
    return render(request, 'success.html')
