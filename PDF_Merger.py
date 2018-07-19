#Import libraries
from PyPDF2 import PdfFileMerger
import os

#Path loading
path = os.getcwd()
# or load your path into a string above
# path = 'C:/path'

pdf_list = os.listdir(path)
#Load the PDF
pdf_merger = PdfFileMerger()
for pdf in pdf_list:
    pdf_merger.append(open(path + str(pdf), 'rb'))

#Write to PDF
with open(path + 'output.pdf', 'wb') as file_out:
    merger.write(file_out)
