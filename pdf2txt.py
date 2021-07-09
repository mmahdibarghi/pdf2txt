#install tesseract : this is a open sourse OCR project By Google
#install persian language for tesseract



# import the following libraries
# will convert the image to text string
import pytesseract

# adds image processing capabilities
from PIL import Image

#split pdf
from PyPDF2 import PdfFileWriter, PdfFileReader
#convert pdf to image
from pdf2image import convert_from_path
#############################################################




## Split PDF

# add your pdf in project folder and change "biganeh.pdf" to your pdf name
inputpdf = PdfFileReader(open("biganeh.pdf", "rb"))
result=""
for i in range(inputpdf.numPages):
    #make pdf
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    name = "document-page%s.pdf" % i
    with open(name, "wb") as outputStream:
        output.write(outputStream)
##############################################
