from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__) #Name of Current instance offlask
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from app import routes

socketio.run(app)