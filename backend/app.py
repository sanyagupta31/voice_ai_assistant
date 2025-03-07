from flask import Flask, request, jsonify
from speech_processing import speech_to_text
from disease_detection import detect_disease
from text_to_speech import text_to_speech
import os

app = Flask(__name__)

@app.route('/voice-input', methods=['POST'])
def voice_input():
    # User से voice file receive करो
    audio_file = request.files['audio']
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)

    # Speech-to-Text Convert करो
    user_text = speech_to_text(audio_path)

    # Disease Detect करो
    response_text = detect_disease(user_text)

    # Text-to-Speech में Convert करके response.mp3 में save करो
    text_to_speech(response_text, "response.mp3")

    return jsonify({"response": response_text, "audio_file": "response.mp3"})

if __name__ == '__main__':
    app.run(debug=True)
