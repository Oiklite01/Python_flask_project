from PIL import Image

image = Image.open(r'C:\Users\arora\Desktop\Coding\Python Flask project main\test\ruled.jpg')
# w,h=image.size
print(image.size[1],end="")