from PIL import Image

image = Image.open("ODD_Smile.jpg")
print(image)
print(image.format, image.size, image.mode)
image.show()