from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'meuSegredo'
socketio = SocketIO(app)

messages = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(message):
    global messages

    if message:
        messages.append(message)
        emit('message', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app=app, debug=True)
