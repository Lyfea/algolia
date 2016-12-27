#!flask/bin/python

from sys import argv
import server
import data

if __name__ == "__main__":
    data.init(argv[1])
    server.init()
