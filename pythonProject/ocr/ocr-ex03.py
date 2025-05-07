from PIL import Image
import pytesseract

image_path = r"한글영어.png"
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
test = pytesseract.image_to_string(Image.open(image_path), lang="kor+eng")

print(test)

with open(r'한글영어변환.txt', 'w', encoding='utf8') as f:
    f.write(test)
