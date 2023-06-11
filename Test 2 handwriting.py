from flask import Flask, render_template, request
import speech_recognition as sr
import textwrap
from PIL import Image, ImageDraw, ImageFont
from deepmultilingualpunctuation import PunctuationModel
import re
model=PunctuationModel()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',disp="Block",disp2="None")

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
        
        
        #speech to text
        r = sr.Recognizer()
        
        # Read the audio file
        audio = sr.AudioFile(file)
        
        # Convert speech to text
        with audio as source:
            r.dynamic_energy_threshold = True
            r.adjust_for_ambient_noise(source=source, duration=0.3)
            audio_data = r.record(source)
            raw_text = r.recognize_google(audio_data,language="en-IN")# MAIN TEXT CONVERTED 
        ptext=model.restore_punctuation(raw_text)
        pfilter=re.compile('([?!.]\s*)')
        split_text=pfilter.split(ptext)
        text=''.join([i.capitalize() for i in split_text])

        return render_template('index.html',text=text,disp="none" ,disp2="block")
        
    return 'Invalid file format'

@app.route('/process',methods=['POST'])
def process():
    # Load the font
    text=request.form['final']
    font = ImageFont.truetype('C:\Windows\Fonts\BRADHITC.TTF', size=52)

    # Ruled Page vector final (converted to jpg)
    image = Image.open(r'C:\Users\arora\Desktop\Coding\Python Flask project main\test\ruled.jpg')

    
    draw = ImageDraw.Draw(image)
    #draw.text((190, 220), text, font=font, fill=(0,0,0,20))
    #implementing wrap text feature for 1 page
    lines=textwrap.wrap(text,width=65)
    y_text = 263
    for line in lines:
        width, height = font.getsize(line)
        draw.text((300,y_text),line,font=font,fill='blue',stroke_fill='blue',stroke_width=1)
        y_text += 62.4
        if(y_text>image.size[1]):
            break

    
    image.save('static/temp.png')
    image_path = 'static/temp.png'
    return render_template('result.html',image_path=image_path)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['wav', 'mp3']

if __name__ == '__main__':
    app.run(debug=True)