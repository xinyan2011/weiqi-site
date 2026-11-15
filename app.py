from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "围棋网站起步中"