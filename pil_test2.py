from PIL import Image

image = Image.open(r'C:\Users\arora\Desktop\Coding\Python Flask project main\test\testing.jpg')
w,h=image.size
print(w,h,end="")