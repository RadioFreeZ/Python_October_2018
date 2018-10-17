from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'index.html')
def submit(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if('counter' in request.session):
            request.session['counter'] +=1
        else:
            request.session['counter'] = 1
        return redirect('/result')
    else:
        return redirect('/')
def add(request):
    return render(request,'result.html')
