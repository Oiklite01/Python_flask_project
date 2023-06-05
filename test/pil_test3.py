from PIL import Image, ImageDraw, ImageFont

width, height = 800, 800
background_color = (255, 255, 255)  # White color (RGB)
image = Image.new("RGB", (width, height), background_color)

draw = ImageDraw.Draw(image)

line_color = (200, 200, 200)  # Light gray color (RGB)
line_interval = 20
for y in range(0, height, line_interval):
    line_start = (0, y)
    line_end = (width, y)
    draw.line([line_start, line_end], fill=line_color)

margin = 50
header_text = "Notebook Page"
header_font = ImageFont.truetype("arial.ttf", 30)  # Choose your desired font
header_color = (0, 0, 0)  # Black color (RGB)
header_position = (margin, margin)
draw.text(header_position, header_text, font=header_font, fill=header_color)

image.save("test/notebook_page.png")