from flask import Flask, render_template, request, jsonify
from robot_ import robot_function
from kaitom_tts import generate_and_play_audio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robot_control', methods=['POST'])
def robot_control():
    action = request.form.get('action')
    text = request.form.get('text')  # Get the text input
    if action:
        robot_function(action)
        return jsonify({'message': 'Command sent to the robot: ' + action})
    elif text:
        generate_and_play_audio(text)  # Call the TTS function with the text input
        return jsonify({'message': 'Text sent for speech generation: ' + text})
    else:
        return jsonify({'message': 'Invalid request'})


if __name__ == '__main__':
    app.run()
