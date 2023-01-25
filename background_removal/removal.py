from rembg import remove
from PIL import Image
image_input = Image.open("lal2.jpeg")
output = remove(image_input)
output.save('ab.png')

