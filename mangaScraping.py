import sys 
import bs4 as bs
import requests as request
import time

class mangaFinder():
    def __int__(self,url,start,end):
        self.url = url
        self.chStart = start
        self.chEnd = end   
        self.domain = self.url[:self.url.find('.')]
    def domainSplitter(self):
        if self.domain == 'https://mangafox':
            self.mangafoxDowloadImage()
        else:
            print('not supported')
    def mangafoxDowloadImage(self):
        sauce = request.get('{}'.format(), verify=False) # to do get the link
        soup = bs.BeautifulSoup(sauce.text, 'html.parser')
        #  initiation of Bs object
        end = url.find('html')-1
        start = url.rfind('/')+1
        fileName = url[start:end]
        # name of the jpg file    
        result = soup.find('img')        
        stringResult = str(result)
        #find the tag whit the link of the image 
        start = stringResult.find('src=')
        urlImage = stringResult[start:]
        end = urlImage.find(' ')-1
        urlImage = urlImage[5:end]
        urlImage = urlImage.replace('amp;','')
        # get the link of the image by delete the 'junk text' of the tag
        
        img_data = request.get(urlImage).content
        with open('{}.jpg'.format(fileName), 'wb') as handler:
            handler.write(img_data)        
        #dowload the image 
    def mangafoxGetChapter(self):
        #initiation of bs
        sauce = request.get(self.url, verify=False)
        soup = bs.BeautifulSoup(sauce.text, 'html.parser')
        allResult = soup.find_all('a')
        
        resultatChapter = [] # list of chapter
        
        temp = [] # list of tag whitout the chapter
        # get tag whit chapter
        for result in allResult:
            testAgent = '//mangafox.me/manga/kobayashi_san_chi_no_maid_dragon/'
            testAgent2 = 'title'
            
            if  testAgent in str(result) and testAgent2 in str(result):
                pass
            else:
                temp.append(result)
        # delete the tag whiout the chapter
        for el in temp:
            allResult.remove(el)
        # extract the link out of the tag
        for result in allResult:
            start = str(result).find('href="') +6
            end = str(result).find('" title')
            link = 'https:'+str(result)[start:end]
        
                    