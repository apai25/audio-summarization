import speech_recognition as sr
from PIL import Image
import pytesseract
from summarizer import Summarizer

model = Summarizer()

def audio_to_string(audio_path):

    r = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)

    with audio_file as source:
        audio = r.record(source)
    
    text = r.recognize_google(audio)
    return text

def text_to_string(path):

    with open(path, 'r') as file:
        data = file.read().replace('\n', '')
    
    return data

def summarize(text):
    global model
    
    summarized_text = model(text, ratio=0.2)

    return summarized_text

if __name__ == '__main__':
    print('libraries imported')