from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
    return render_template("forms.html")

@app.route('/result', methods=['POST'])

def create_user():
    print("Got Post Info")
    valid = True
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    if language == "C++":
        language = "C++!? You Maniac!"
    comment = request.form['comment']
    if len(name) < 1:
        flash("Name cannot be empty", 'Name')
        valid = False
    if len(comment) < 1:
        flash("Comment cannot be empty",'Comment')
        valid = False
    if len(comment) > 120:
        flash("Comment cannot have more than 120 characters", 'Comment')
        valid = False
    if valid:
        return render_template("result.html", name=name,location=location,language=language,comment=comment)
    else:
        return redirect("/")


@app.route('/danger')

def danger():
    print("User tried to enter danger!")
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
