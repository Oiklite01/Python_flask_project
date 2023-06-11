from PIL import Image,ImageDraw,ImageFont
import textwrap
f=open('test/para.txt','r')
data=f.read()
lines=textwrap.wrap(data,width=69)
y_text = 263

# font=ImageFont.truetype('C:/Windows/Fonts/BAUHS93.TTF',size=50)#tested random fonts
# font = ImageFont.truetype('C:\Windows\Fonts\BRADHITC.TTF', size=52)
font = ImageFont.truetype(r'C:\Users\arora\AppData\Local\Microsoft\Windows\Fonts\Anjali2-Regular.ttf' , size=52)
image = Image.open('test/ruled.jpg')
draw=ImageDraw.Draw(image)


for line in lines:
    # width, height = font.getsize(line)
    draw.text((300,y_text),line,font=font,fill='black')
    y_text += 62.4
    if(y_text>image.size[1]):
        break
        

    #draw.text((200,200),data,font=font,fill='blue',align='left',stroke_fill='red',stroke_width=5) #Testing strokes
image.save('test/temp.png')