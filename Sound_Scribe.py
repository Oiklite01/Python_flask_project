#Dependencies
from flask import Flask, render_template, request
import speech_recognition as sr
import textwrap
from pydub import AudioSegment
from PIL import Image, ImageDraw, ImageFont
from deepmultilingualpunctuation import PunctuationModel
import re

#Required SetUp
model=PunctuationModel()
app = Flask(__name__)
AudioSegment.converter = "C:/ffmpeg/ffmpeg-2023-06-19-git-1617d1a752-full_build/bin/ffmpeg.exe"
AudioSegment.ffmpeg = "C:/ffmpeg/ffmpeg-2023-06-19-git-1617d1a752-full_build/bin/ffmpeg.exe"
AudioSegment.ffprobe = "C:/ffmpeg/ffmpeg-2023-06-19-git-1617d1a752-full_build/bin/ffprobe.exe"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html',disp="Block",disp2="None")


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('index.html',text=recText,disp="none" ,disp2="block")

    # Check if a file was submitted
    if 'file' not in request.files:
        return 'No file found'
    file = request.files['file']
    # Check if the file is empty
    if file.filename == '':
        return 'No file selected'
    # Check if the file is valid audio
    if file and allowed_file(file.filename):
        # Read the audio file
        audio = sr.AudioFile(file)
        # Convert speech to text and process it
        text=format(audio)
        return render_template('index.html',text=text,disp="none" ,disp2="block")
        
    return 'Invalid file format'


@app.route('/tth',methods=['POST'])
def tth():
    return render_template('index.html',text='',disp="none" ,disp2="block")

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    ##Add the implementation to save and convert the audio file to right specs to be read by sr
    sound = AudioSegment.from_file(audio_file)
    sound.export(audio_file,format="wav")
    # Read the audio file
    audio = sr.AudioFile(audio_file)
    # Convert speech to text and process it
    global recText
    try:
        recText=format(audio)
    except:
        recText='Audio Not Found'
    return ''




@app.route('/process',methods=['POST'])
def process():
    
    text=request.form['final']
    a=text.split('\r\n')
    # Load the font
    font = ImageFont.truetype('fonts/Myfont-Regular.ttf',size=54)
    # Ruled Page vector final (converted to jpg)
    image = Image.open('static/images/ruled1.jpg')
    draw = ImageDraw.Draw(image)
    y_text = 277
    #implementing wrap text feature for 1 page
    for split_text in a:
        lines=textwrap.wrap(split_text,width=75)
        for line in lines:
            draw.text((300,y_text),line,font=font,fill='#000c1f')
            y_text += 62.3
            if(y_text>image.size[1]):
                break   
    image.save('static/images/temp.png')
    return render_template('result.html')




def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['wav', 'mp3']




def format(audio):
    r = sr.Recognizer()
    with audio as source:
        r.dynamic_energy_threshold = True
        audio_data = r.record(source)
        raw_text = r.recognize_google(audio_data,language="en-IN")# MAIN TEXT CONVERTED 
    ptext=model.restore_punctuation(raw_text)
    pfilter=re.compile('([?!.]\s*)')
    split_text=pfilter.split(ptext)
    text=''.join([i.capitalize() for i in split_text])
    return text




if __name__ == '__main__':
    app.run(debug=True)