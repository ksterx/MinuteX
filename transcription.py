import speech_recognition as sr


def get_transcript(audio_file):
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable
    with sr.AudioFile(audio_file) as source:
        audio_text = r.record(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        print("Converting audio transcripts into text ...")
        text = r.recognize_google(audio_text)
        return text

    except:
        print("Sorry.. run again...")
