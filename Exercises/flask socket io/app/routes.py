from app import app
from app import socketio
from flask import render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True, async_mode=socketio.async_mode)

#SOCKETS
@socketio.on('connectFirstTime', namespace='/test')
def connectFirstTime(message):
    session[str(message["userId"])] = 0;
    emit('my_response',{'data': message['data'] + " By: " + str(message["userId"]) + " *score = " + str(session[str(message["userId"])])})

@socketio.on('my_event', namespace='/test')
def test_message(message):
    session[str(message["userId"])] += 5;
    print(session[str(message["userId"])])
    emit('my_response',
         {'data': message['data'] + " By: " + str(message["userId"]) + " *score = " + str(session[str(message["userId"])])})


@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    emit('my_response',
         {'data': message['data'] + " By: " + str(message["userId"]) + " *score = " + str(session[str(message["userId"])])},
         broadcast=True)


@socketio.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    emit('my_response',
         {'data': 'In rooms: ' + ', '.join(rooms())})


@socketio.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    emit('my_response',
         {'data': 'Left rooms: ' + ', '.join(rooms())})


@socketio.on('my_room_event', namespace='/test')
def send_room_message(message):
    emit('my_response',{'data': message['data'] + " By: " + str(message["userId"]) + " *score = " + str(session[str(message["userId"])])},room=message['room'])

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)

