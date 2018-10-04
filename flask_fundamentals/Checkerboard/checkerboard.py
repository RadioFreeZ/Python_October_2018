from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')

def index():
    # for i in range(8):
    return render_template("checkerboard_basic.html")



@app.route('/<int:x>/<int:y>')

def nums(x,y):
    return render_template("checkerboard_complex.html",x = x, y= y)

if __name__=="__main__":
    app.run(debug=True)
