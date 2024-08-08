from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    __path__="C:/Users/Ritesh/OneDrive/Pictures"
    return __path__
