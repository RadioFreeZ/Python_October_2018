from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(1,101)
    if 'guess' not in session:
        session['guess']=0
    return render_template('main.html', number = session['number'], guess = session['guess'])

@app.route('/guess', methods=['POST'])
def guessaroni():

    session['guess'] = int(request.form['userGuess'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetaroni():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)
