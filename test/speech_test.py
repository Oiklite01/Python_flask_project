import speech_recognition as sr
from deepmultilingualpunctuation import PunctuationModel
import re
model = PunctuationModel()
r = sr.Recognizer()
# Read the audio file
audio = sr.AudioFile(r'C:\Users\arora\Downloads\test audio 3.wav')

# Convert speech to raw_text
with audio as source:
    r.energy_threshold=0
    audio_data = r.record(source)
    raw_text = r.recognize_google(audio_data,language="en-IN")
text=model.restore_punctuation(raw_text)
punc_filter = re.compile('([.!?]\s*)')
split_with_punctuation = punc_filter.split(text)
final = ''.join([i.capitalize() for i in split_with_punctuation])
print(final)