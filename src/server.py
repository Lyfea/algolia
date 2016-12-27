#!flask/bin/python

from flask import Flask
from flask import request
import searcher

app = Flask(__name__)

@app.route('/1/queries/count/<date>')
def count(date):
    return str(searcher.count(date))

@app.route('/1/queries/popular/<date>')
def popular(date):
    size = int(request.args['size'])
    return str(searcher.popular(date, size))

def init():
    app.run(debug=False)

if __name__ == "__main__":
    print(argv[1])
    init()
