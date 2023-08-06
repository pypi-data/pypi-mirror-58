
from bs4 import BeautifulSoup

import PIL.Image

import pytesseract
import os

home = os.environ.get('Tesseract-OCR')
print (home)


def img2txt(path):
    img=PIL.Image.open(path)
    pytesseract.pytesseract.tesseract_cmd=(home)
    result=pytesseract.image_to_string(img)
    with open(r"C:\Users\Dell\Downloads\Image_To_Text.txt", "w") as text_file:
        text_file.write(result)
        ans=print("Check your download folder Image_To_Text.txt \n "+result)
    return(ans)


                        #flash('File successfully uploaded')
                        #flash('Check your download folder Image_To_Text.txt')


