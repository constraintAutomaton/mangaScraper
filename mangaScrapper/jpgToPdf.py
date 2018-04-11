from fpdf import FPDF
import cv2
import os


class PDF(FPDF):
    def __init__(self,chapterName, imageList=[]):
        FPDF.__init__(self)
        self.imageList=imageList
        self.sizePdfPortraitX = 210
        self.sizePdfPaysageX = 240
        self.imageCount = 0
        self.chapterName = chapterName+'.pdf' 
    def chapter_body(self):
        if self.imageCount<len(self.imageList):
            self.image(self.imageList[self.imageCount],0,0,self.sizePdfPortraitX)
            self.ln()
            self.imageCount += 1
    def print_chapter(self):
        self.add_page()
        self.chapter_body()
    def Change_image_list(self,imageList):
        self.imageList = imageList
    def run(self):
        if not os.path.exists('pdf'):        
            os.makedirs('pdf')        
        for  image in self.imageList:
            self.print_chapter()
        self.output(os.path.join('pdf',self.chapterName),'F')
