from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def index():
    return "Hello World!"

@app.route("/play")

def three_box():
    return render_template("play_1.html")

@app.route('/play/<int:x>')

def x_boxes(x):
    return render_template("play_2.html", num = x)
@app.route('/play/<int:x>/<col>')

def x_boxes_color(x,col):
    return render_template("play_3.html", num = x, color = col)

if __name__=="__main__":
    app.run(debug=True)
