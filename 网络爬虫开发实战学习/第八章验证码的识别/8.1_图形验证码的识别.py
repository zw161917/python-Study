import pytesseract
from PIL import Image
inage = Image.open('code1.jpg')
result = pytesseract.image_to_text(inage)
print(result)

