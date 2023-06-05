from PIL import Image,ImageDraw,ImageFont
import textwrap
f=open('test/para.txt','r')
data=f.read()
lines=textwrap.wrap(data,width=75)
y_text = 225

# font=ImageFont.truetype('C:/Windows/Fonts/BAUHS93.TTF',size=50)#tested random fonts
font = ImageFont.truetype('C:\Windows\Fonts\BRADHITC.TTF', size=55)
image = Image.open('C:/Users/arora/Desktop/Coding/Python Flask project main/test/testing.jpg')
draw=ImageDraw.Draw(image)


for line in lines:
    width, height = font.getsize(line)
    draw.text((200,y_text),line,font=font,fill='black',stroke_fill='black',stroke_width=1)
    y_text += 90
    #draw.text((200,200),data,font=font,fill='blue',align='left',stroke_fill='red',stroke_width=5) #Testing strokes


image.save('test/temp.png')