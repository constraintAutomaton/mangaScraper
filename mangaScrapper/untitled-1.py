from fpdf import FPDF


class PDF(FPDF):
    def __init__(self,imageList):
        FPDF.__init__(self)
        self.imageList=imageList
        self.sizePdfPortraitX = 200
        self.sizePdfPaysageX = 240
        
    def chapter_body(self,a):
        self.image(self.imageList[0],0,0,210)
        self.ln()
    def print_chapter(self,a):
        self.add_page()
        self.chapter_body(1)
    

# Instantiation of inherited class
pdf = PDF(['542106.jpg','542106.jpg','542106.jpg'])
pdf.print_chapter(1)
pdf.print_chapter(1)
pdf.output('tuto.pdf', 'F')