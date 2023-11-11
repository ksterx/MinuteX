

from flask import Flask, request, jsonify
import speech_recognition as sr
from pydub import AudioSegment
import numpy as np
import openai
import transcription

app = Flask(__name__)

# Initialize OpenAI API
openai.api_key = 'your_openai_api_key'

# Initialize Speech Recognition
r = sr.Recognizer()

@app.route('/start', methods=['POST'])
def start():
    audio_data = request.files['audio'].read()
    audio = AudioSegment.from_file(audio_data, format="wav")
    audio.export(" return jsonify({"transcription": text}), 200

audio.export("meeting.wav", format="wav")
    return jsonify({"message": "Audio received and saved"}), 200

@app.route('/transcribe', methods=['GET'])
def transcribe():
    with sr.AudioFile('meeting.wav') as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
   text-davinci-002",
        prompt=transcript,
        temperature=0.5,
        max_tokens=100
    )
    return jsonify({"advice": response.choices[0].text.strip()}), 200

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/advice', methods=['GET'])
def advice():
    transcript = transcription.get_transcript('meeting.wav')
    response = openai.Completion.create(
        engine="}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    line-height: 1.6em;
}

header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

header h1 {
    margin: 0;
}

header p {
    margin-top: 10px;
    font-style: italic;
}

main {
    padding: 20px;
    max-width: 800px;
    margin: 20px auto;
}

#controls {
    text-align: center;
    margin-bottom: 20px;
}

#start-meeting {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 18px;
}

#start-meeting:hover {
    background-color: #444;
}

#transcript, #advice {
    background-color: #fff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
}

#transcript h2, #advice h2 {
    margin-bottom: 10px;
}

footer {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: #fff;
    position: fixed;
    bottom: 0
