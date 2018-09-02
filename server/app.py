"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from route import *
import os

app = Flask(__name__,template_folder='C://Users/Saket/Desktop/Preciso/Addin',static_folder='C://Users/Saket/Desktop/Preciso/Addin/static')

wsgi_app = app.wsgi_app

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '55555'))
    except ValueError:
        PORT = 55555
    app.debug=True #adding this code from flask tutorial from tutpoint says the app will reload if changes made lets see
    app.run(HOST, PORT)
    app.run(debug=True)
