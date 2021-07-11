from util import summarize, audio_to_string
import sounddevice as sd
import wavio

fs = 44100  
seconds = 20

summary = ''
while True:
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  
    audio_path = 'audio.wav'

    wavio.write(audio_path, myrecording, fs, sampwidth=2)  
    audio_content = audio_to_string(audio_path) + '.'

    summary += summarize(audio_content)

    with open('summary.txt', 'w') as summary_file:
        summary_file.write(summary)
