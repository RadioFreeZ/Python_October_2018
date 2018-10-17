from django.shortcuts import render, HttpResponse, redirect
import datetime
def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request,'index.html')

def submit(request):
    if request.method == "POST":
        if 'big_font' in request.POST:
           showbig = 1.7
        else:
           showbig = 1
        temp_list = request.session['words']
        temp_list.append({"word": request.POST['word'], "color": request.POST['color'], "font": showbig, "time": str(datetime.datetime.now())})
        request.session['words'] = temp_list
        return redirect('/session_words')
    else:
        return redirect('/session_words')
def clear(request):
    del request.session['words']
    return redirect('/session_words')
