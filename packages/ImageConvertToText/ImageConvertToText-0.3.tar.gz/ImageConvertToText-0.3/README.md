# Example Package

# Download Tesseract-OCR first.
Follow the link:

 #For WINDOWS:-
  https://github.com/UB-Mannheim/tesseract/wiki

#For macOS 
https://github.com/scott0123/Tesseract-macOS


#Set Environment variable to :-

Variable:-Tesseract-OCR

Path:- Path where Tesseract-OCR is installed like(C:\Program Files\Tesseract-OCR\tesseract.exe)


#type following code in python shell after installing library.
1st step :
 from   ImageConvertToText   import ImageTextConverter  

2nd step:
ImageTextConverter.img2txt('Path_of_your_Image_file')


In ('Path_of_your_Image_file') here write the path of image file that u want extract the text from.
for example 'ImageTextConverter.img2txt(r'C:\Users\Dell\Downloads\Images\PythonKnowledgeGraph.png')'like that only
