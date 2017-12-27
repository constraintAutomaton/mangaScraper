import sys 
import bs4 as bs
import requests as request
import time
import os

def find_nth(string,substring,nb,direction = 'f'):
    
    
    beg = string.find(substring)
    if direction == 'f':
        while nb>1 and beg<len(string):
            beg = string.find(substring,beg+1)
            nb -= 1
    else:
        past = ''
        result = [beg]
        while True:
            
            beg = string.find(substring,beg+1)
            result.append(beg)
            if result[len(result)-1] ==-1:
                break
        beg = result[len(result)-nb-1]
    result = beg
    return result
class mangaFinder():
    def __init__(self,url,start,end,folder):
        self.url = url
        self.chStart = start
        self.chEnd = end   
        self.domain = self.url[:self.url.find('.')]
        self.folder = folder
        
    def domainSplitter(self):
        if self.domain == 'http://mangafox':
            self.mangafoxDowload()
        else:
            print('not supported')
            
    def mangafoxDowload(self):
        allChapt = self.mangafoxGetChapter() # get all the chapter ask by the user
        
        for urlCh in allChapt: 
            try:
                folder = self.mangafoxNameFolder(urlCh)
                os.makedirs(r'{}\{}'.format(self.folder,folder))
            except:
                pass
            
            allPage = self.mangafoxGetAllPageChapter(urlCh) # get all the page of the user
            
            for urlPage in allPage:
                sauce = ''
                while sauce == '':
                    try:
                        sauce = request.get(urlPage, verify=False)
                    except:
                        time.sleep(5)
                        continue                
                 
                soup = bs.BeautifulSoup(sauce.text, 'html.parser')
                #  initiation of Bs object
                
                end = urlPage.find('html')-1
                start = urlPage.rfind('/')+1
                fileName = urlPage[start:end]
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
                try: # delete the file if it already exist
                    self.manageImage(fileName,folder)
                except:
                    os.remove('{}.jpg'.format(fileName))
                    
                #dowload the image 
                
    def mangafoxGetChapter(self):
        #initiation of bs
        sauce = ''
        while sauce == '':
            try:
                sauce = request.get(self.url, verify=False)
            except:
                time.sleep(5)
                
                continue        
            
        soup = bs.BeautifulSoup(sauce.text, 'html.parser')
        allResult = soup.find_all('a')
        
        resultatChapter = [] # list of chapter
        
        temp = [] # list of tag whitout the chapter
        # get tag whit chapter
        for result in allResult:
            testAgent = self.url[5:] # false
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
            link = 'http:'+str(result)[start:end]
            # get the chapter input
            start = link.rfind('c')+1
            end = link.rfind('/')
            numberchapt = link[start:end]
            for x in range(0, 2):
                if numberchapt[0] == '0':
                    numberchapt = numberchapt[1:]
            if float(numberchapt)<=self.chEnd and float(numberchapt)>=self.chStart:
                resultatChapter.append(link)     
        
        resultatChapter.reverse()
        return resultatChapter
    def mangafoxGetAllPageChapter(self,chapterUrl):
        
        #initiation of bs
        sauce = ''
        while sauce == '':
            try:
                sauce = request.get(chapterUrl, verify=False)
            except:
                time.sleep(5)
                print('page')
                continue
        soup = bs.BeautifulSoup(sauce.text, 'html.parser')
        allResult = soup.find_all('a')
        
        #find select tag who contains the text of the page of the chapter
        allResult = soup.find_all('select') 
        tagNumberPage = str(allResult[1])
        
        start = find_nth(tagNumberPage,'value="',2,'r')+7
        end = tagNumberPage.find('"',start)
        numberPage = int(tagNumberPage[start:end])
        listNumberPage =[]
        
        while  numberPage>0:
            listNumberPage.append(numberPage)
            numberPage-=1
        listNumberPage.reverse()
        listPageUrl = []
        
        for page in listNumberPage:
            end = chapterUrl.rfind('/')+1
            urlPage = chapterUrl[0:end]+str(page)+'.html'
            listPageUrl.append(urlPage)
       
        return listPageUrl
    def mangafoxNameFolder(self,urlCh):
        start = find_nth(urlCh,'/',4,'r')+1
        name = urlCh[start:]
        loopName = name # can't loop and modify
        
        for caracter in loopName:
            
            if caracter=='_' or caracter=='/' :
    
                name = name.replace(caracter,' ')
        name = name.replace('1.html','')
        return name
        
    def manageImage(self,image,folder):
        os.rename(r'{}.jpg'.format(image), r"{}\{}\{}.jpg".format(self.folder,folder,image))
        