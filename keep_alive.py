from flask import Flask
from threading import Thread


app = Flask('')

@app.route('/')
def home():
    html = open("index.html",'r')
    htmltext= html.read()
    return htmltext


def run():
    app.run(debug=True)

def keep_alive():
    t = Thread(target=run)
    t.start()
