# coding: utf-8
import sys
import re
import os
sys.path.append(os.path.join('..','mangaScrapper',))
from jpgToPdf import PDF

os.chdir(os.path.join('test_folder'))
listFile = os.listdir(r'vagabond v01 c001')
listImage = []
for file in listFile:
    if '.jpg' in file:
        listImage.append(file)     
listImage = sorted(listImage, key=lambda x: (int(re.sub('\D','',x)),x))
print(listImage)
os.chdir(os.path.join(r'vagabond v01 c001'))
testPdf = PDF('vagabon',imageList=listImage)

testPdf.run()
#for i in range(10):
    #testPdf.print_chapter()
#testPdf.output('test.pdf','F')            
        

