"""for the moment it can't make the image in Landscape"""
from fpdf import FPDF
import cv2
import os
import shutil


class PDF(FPDF):
    """image have to be in the same folder"""
    def __init__(self,chapterName='?', imageList=[]):
        FPDF.__init__(self)
        self.imageList=imageList
        self.sizePdfPortraitX = 210
        self.sizePdfPortraitY = 240
        self.sizePdfLandscapeX = 240
        self.sizePdfLandscapeY = 210
        self.imageCount = 0
        self.chapterName = chapterName+'.pdf' 
    def chapter_body(self):
        if not os.path.exists(os.path.join(self.workingPath,'pdf')):        
            os.makedirs(os.path.join(self.workingPath,'pdf')) 
        if not os.path.exists(os.path.join(self.workingPath,'pdf','temp')):        
            os.makedirs(os.path.join(self.workingPath,'pdf','temp'))        
        if self.imageCount<len(self.imageList):
            currentImage, size = self.image_management(self.imageList[self.imageCount])
            self.image(currentImage,0,0,size)
            self.ln()
            self.imageCount += 1
    def print_chapter(self):
        self.add_page()
        self.chapter_body()
    def Change_image_list(self,imageList):
        self.imageList = imageList
        self.workingPath =imageList[0][0:imageList[0].rfind('\\')]        
    def change_pdf_name(self,name):
        self.chapterName = name+".pdf"
    def image_management(self,image):
        '''resize image depending of the size of the image'''

        img = cv2.imread(image)
        height, width, channel = img.shape
        if height>width:
            resizeIamge = cv2.resize(img,(self.sizePdfPortraitX,self.sizePdfPortraitY))
            size = self.sizePdfPortraitX
            
        else:
            resizeIamge = cv2.resize(img,(self.sizePdfLandscapeX,self.sizePdfLandscapeY))
            size = self.sizePdfLandscapeX
            self.orientation = 'L'
        imageName = image[0:image.find('.')]+'pdf'+image[image.find('.'):]
        imageName = imageName[imageName.rfind('\\')+1:]
        cv2.imwrite(os.path.join(self.workingPath,'pdf','temp',imageName),img)
        return (os.path.join(self.workingPath,'pdf','temp',imageName),size)
    def run(self):       
        for  image in self.imageList:
            self.print_chapter()
        self.output(os.path.join(self.workingPath,'pdf',self.chapterName),'F')
        shutil.rmtree(os.path.join(self.workingPath,'pdf','temp'), ignore_errors=True)
    def restart(self):
        self.__init__()
        
        
