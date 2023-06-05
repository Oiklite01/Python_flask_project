from flask import Flask, render_template, request
import speech_recognition as sr
from PIL import Image, ImageDraw, ImageFont

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
            # font_path = f"fonts\BRADHITC.ttf"

        # Load the font
        font = ImageFont.truetype('C:\Windows\Fonts\BRADHITC.TTF', size=54)

        # Create a blank image with white background
        image = Image.open(r'C:\Users\arora\Desktop\Coding\Python Flask project main\test\testing.jpg')

        # Draw the text on the image using the loaded font
        draw = ImageDraw.Draw(image)
        draw.text((190, 220), text, font=font, fill=(0,0,0,20))

        # Save the image as a temporary file
        image.save('static/temp.png')
        image_path = 'static/temp.png'
        return render_template('result.html',image_path=image_path)
    
    return 'Invalid file format'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['wav', 'mp3']

if __name__ == '__main__':
    app.run(debug=True)