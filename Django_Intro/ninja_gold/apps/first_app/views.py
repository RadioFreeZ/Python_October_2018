from django.shortcuts import render, HttpResponse, redirect
import random, datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activitylog'] = ''
    return render(request, 'index.html')
def process(request):
    if request.method == 'POST':
        location = request.POST['building']
        if location == 'farm':
            money = random.randrange(10,21)
            request.session['gold'] += money
        elif location == 'cave':
            money = random.randrange(5,11)
            request.session['gold'] += money
        elif location == 'house':
            money = random.randrange(2,6)
            request.session['gold'] += money
        elif location == 'casino':
            money = random.randrange(random.randrange(-50,0),random.randrange(0,51))
            request.session['gold'] += money

        if money < 0:
            money *= -1
            request.session['activitylog'] += (f"<p class='text-danger'>Entered a {location} and lost {money} gold...Ouch..({datetime.datetime.now()})</p>")
        else:
            request.session['activitylog'] += (f"<p class='text-success'>Earned {money} gold from the {location}! ({datetime.datetime.now()})</p>")

        if request.session['gold'] < 0:
            request.session['activitylog'] += (f"<p class='text-danger'>Watch out the Mob is coming to collect!!!!!</p>")

        return redirect('/')
