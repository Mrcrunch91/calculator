import os 
import threading, time
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from flask import app


def before_all(context):
    context.server = simple_server.WSGIServer(("0.0.0.0", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()



def after_all(context):
    context.server.shutdown()
    context.pa_app.join()