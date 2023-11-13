import io

import speech_recognition as sr
from flask import Flask, jsonify, request
from openai import OpenAI
from pydub import AudioSegment

import backend.transcription as transcription

app = Flask(__name__)

client = OpenAI(api_key="")

# Initialize Speech Recognition
r = sr.Recognizer()


@app.route("/start", methods=["POST"])
def start():
    audio_data = request.files["audio"].read()
    audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
    audio.export(" meeting.wav", format="wav")
    return jsonify({"message": "Audio received and saved"}), 200


@app.route("/transcribe", methods=["POST"])
def transcribe():
    with sr.AudioFile("meeting.wav") as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    response = client.completion.create(
        engine="text-davinci-002", prompt=text, temperature=0.5, max_tokens=100
    )
    return jsonify({"advice": response.choices[0].text.strip()}), 200


@app.route("/advice", methods=["GET"])
def advice():
    transcript = transcription.get_transcript("meeting.wav")
    response = client.completions.create(
        engine="gpt-3.5-turbo", prompt=transcript, temperature=0.5, max_tokens=100
    )
    return jsonify({"advice": response.choices[0].text.strip()}), 200


if __name__ == "__main__":
    app.run(debug=True)
