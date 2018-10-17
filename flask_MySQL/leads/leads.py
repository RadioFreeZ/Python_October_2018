from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
@app.route('/')
def index():
    mysql = connectToMySQL("customers")
    all_clients = mysql.query_db("SELECT * FROM clients")
    print("Fetched all friends", all_clients)
    return render_template('index2.html', clients = all_clients)


if __name__=="__main__":
    app.run(debug=True)
