#install tesseract and add it to the path: this is a open sourse OCR project By Google
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
    # make image
    images = convert_from_path(name)
    images[0].save('page' + str(i) + '.jpg', 'JPEG')

    ######################################
    ## OCR :: image to text
    img = Image.open('page' + str(i) + '.jpg')
    # path where the tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    # converts the image to result and saves it into result variable
    result = result + "\n\n\n\n\n" + pytesseract.image_to_string(img, lang='fas')
    # write text in a text file and save it to source path
with open('resultFile.txt', mode='wb') as file:
    file.write(result.encode("utf-8"))
    # file.write("\n\n\n\npage:  "+str(i)+"\n\n\n\n".encode("utf-8") )

