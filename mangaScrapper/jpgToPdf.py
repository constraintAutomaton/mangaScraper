from fpdf import FPDF


class PDF(FPDF):
    def __init__(self,imageList=[]):
        FPDF.__init__(self)
        self.imageList=imageList
        self.sizePdfPortraitX = 210
        self.sizePdfPaysageX = 240
        self.imageCount = 0
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

