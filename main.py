from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('login')
def login(data):
    print('login username: ' + str(data['username']))


if __name__ == "__main__":
    socketio.run(app)
