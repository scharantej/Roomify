
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import uuid

# Initialize the Flask application
app = Flask(__name__)

# Secret key for session management (should be set to a random string for production)
app.secret_key = 'secret-key'

# List of currently active chat rooms
rooms = {}

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Create a new chat room
@app.route('/create_room', methods=['POST'])
def create_room():
    # Generate a unique room ID
    room_id = str(uuid.uuid4())

    # Store the room in the list of active rooms
    rooms[room_id] = {'messages': []}

    # Redirect to the new room
    return redirect(url_for('room', room_id=room_id))

# Join an existing chat room
@app.route('/join_room', methods=['POST'])
def join_room():
    # Get the room ID from the form
    room_id = request.form['room_id']

    # Check if the room ID is valid
    if room_id not in rooms:
        return redirect(url_for('home'))

    # Redirect to the room
    return redirect(url_for('room', room_id=room_id))

# Chat room route
@app.route('/room/<room_id>')
def room(room_id):
    # Check if the room ID is valid
    if room_id not in rooms:
        return redirect(url_for('home'))

    # Render the room template
    return render_template('room.html', room_id=room_id, messages=rooms[room_id]['messages'])

# Send a message in a chat room
@app.route('/send_message', methods=['POST'])
def send_message():
    # Get the room ID and message from the form
    room_id = request.form['room_id']
    message = request.form['message']

    # Check if the room ID is valid
    if room_id not in rooms:
        return redirect(url_for('home'))

    # Add the message to the room's message list
    rooms[room_id]['messages'].append(message)

    # Redirect back to the room
    return redirect(url_for('room', room_id=room_id))

# Run the Flask application
if __name__ == '__main__':
    app.run()
