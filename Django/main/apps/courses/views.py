from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import Course
def index(request):
    context = {}
    context['courses'] = Course.objects.all()
    return render(request,"index.html", context)

def add(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/courses/')
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        return redirect('/courses')
def confirm(request, id):
    context = {}
    context['course_confirm'] = Course.objects.get(id = id)
    return render(request,"confirmation.html", context)

def delete(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/courses/')
