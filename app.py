from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = input("What is your name?")
    greeting = "Hello [name]!
    return greeting
