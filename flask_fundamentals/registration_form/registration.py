from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-z]')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')

def main():
    return render_template("index.html")

@app.route('/result', methods=["POST"])

def submit():
    valid = True
    if len(request.form['firstName']) < 1:
        flash("Name cannot be blank!", 'firstName')
        valid = False
        print("WHY")
    elif not NAME_REGEX.match(request.form['firstName']):
        flash("Invalid Name!", 'firstName')
        valid = False
    if len(request.form['lastName']) < 1:
        flash("Name cannot be blank!", 'lastName')
        valid = False
    elif not NAME_REGEX.match(request.form['lastName']):
        flash("Invalid Name!", 'lastName')
        valid = False
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'email')
        valid = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
        valid = False
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!", 'password')
        valid = False
    if len(request.form['passwordConfirm']) < 1:
        flash("Password Confirmation cannot be blank!", 'password')
        valid = False
    elif request.form['password'] != request.form['passwordConfirm']:
        flash("password and password confirmation must be the same", 'password')
        valid = False
    if valid == True:
        flash("Success!", 'true')



    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
