from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    if 'count' in session:
        pass
    else:
        session['count'] = 0

    session['count'] += 1
    temp = str(session['count'])
    if session['count'] > 1:
        visit = f"{temp} visits"
    else:
        visit = f"{temp} visit"
    return render_template("index.html", visit = visit)
@app.route('/count', methods=['POST'])
def counter():
    session['count'] += 1
    return redirect("/")
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)
