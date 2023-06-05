from flask import Flask, render_template, request
import speech_recognition as sr


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was submitted
    if 'file' not in request.files:
        return 'No file found'
    
    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return 'No file selected'
    
    # Check if the file is valid audio
    if file and allowed_file(file.filename):
        recognizer = sr.Recognizer()
        
        # Read the audio file
        audio = sr.AudioFile(file)
        
        # Convert speech to text
        with audio as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        
        return text
    
    return 'Invalid file format'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['wav', 'mp3']

if __name__ == '__main__':
    app.run(debug=True)