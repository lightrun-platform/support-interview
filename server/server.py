from flask import Flask
from time import time


app = Flask(__name__)

@app.route('/')
def hello():
    return {'response_code': '200'}


if __name__ == "__main__":
    app.run('0.0.0.0', 8080)
