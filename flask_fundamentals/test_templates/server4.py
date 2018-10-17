from flask import Flask, render_template,request, redirect,
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello"
@app.route('/show')
def show_user():
  return render_template('index4.html', name='Jay', email='kpatel@codingdojo.com')
if __name__=="__main__":
    app.run(debug=True)
