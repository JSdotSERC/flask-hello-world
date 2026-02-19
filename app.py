from flask import Flask
app = Flask(__name__)

@app.route('/')
    name = input("What is your name?")
    print ("Hello [name]!")
    
