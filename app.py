from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello everyone! My name is PyFile, and I am speaking to you from a working Azure Web App!"
    
