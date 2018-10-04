from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/dojo')

def dojo_print():
    return "Dojo!"

@app.route('/say/<name>')

def name_print(name):
    print (name)
    return f"Hi {name}"

@app.route("/repeat/<num>/<word>")

def repeat_print(num,word):
    num = int(num)
    print (num,word)
    ret_string = ""
    for i in range(num):
        ret_string += word +" "
    return ret_string

if __name__=="__main__":

    app.run(debug=True)
