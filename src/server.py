#!flask/bin/python

from flask import Flask
from flask import request
import searcher

app = Flask(__name__)

@app.route('/1/queries/count/<date>', methods=["GET"])
def count(date):
    return str(searcher.count(date))

@app.route('/1/queries/popular/<date>', methods=["GET"])
def popular(date):
    size = int(request.args['size'])
    return str(searcher.popular(date, size))

@app.errorhandler(404)
def not_found(error):
    return "Error 404: Not found"

def init():
    app.run(debug=False)

if __name__ == "__main__":
    print(argv[1])
    init()
