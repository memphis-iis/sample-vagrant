#!/usr/bin/env python

import sys
import traceback
from functools import wraps

from flask import Flask, request, Response

from pymongo import MongoClient

app = Flask(__name__)

# For this demo, we just manually configure everything. "Real" apps would
# probably want to use from_pyfile and/pr
app.config.update(
    DEBUG=True,
    SECRET_KEY='Shhhh.....',
    HOST='0.0.0.0',
    PORT=3000
)

# This isn't the greatest way to handle MongoDB from a Flask app, but for this
# demo we just need a hard-coded db and collection
db = MongoClient()['sample-vagrant']['connects']


def console(s, *args):
    if app.config["DEBUG"]:
        print(s % args if args else s)


def use_error_page(func):
    """Intended to be used to wrap a Flask route function.  Be sure that
    it's the inner-most annotator on the function.
    """
    @wraps(func)
    def wrapper(*args, **kwrds):
        try:
            return func(*args, **kwrds)
        except:
            try:
                console("ERROR HANDLER = GETTING EXCEPTION VALUE")
                etype, evalue, etrace = sys.exc_info()
                txtpre = "Unexpected error:"
                txtpost = '\n'.join(traceback.format_exception(etype, evalue, etrace))
                return txtpre + '\n' + txtpost
            except:
                console("ERROR IN ERROR HANDLER - PUNTING")
                console("%s: %s\n%s", sys.exc_info())
                return abort(500) #Double Whoops!
    return wrapper


def text_entry(dct):
    return "Full Path: " + dct['full_path'] + " \n HEADERS: " + '\n'.join([
        '  headers[%s] => [%s]' % (k,v) for k,v in request.headers
    ])


@app.route('/')
@use_error_page
def main_page():
    data = { 'full_path': request.full_path }
    data.update(dict(request.headers))
    db.insert(data)
    return Response(text_entry(data), mimetype='text/plain')


@app.route('/history')
@use_error_page
def history_page():
    all_recs = [
        text_entry(r) for r in db.find({})
    ]

    delim = '-' * 50
    delim = '\n' + delim + '\n'

    return Response(delim.join(all_recs), mimetype='text/plain')


def main():
    HOST = app.config['HOST']
    PORT = app.config['PORT']
    console("About to start serving on %s:%d", HOST or "[ALL IFaces]", PORT)
    app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()
