import sys 
import bs4 as bs
import requests as request
import time

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
        
        for urlCh in self.mangafoxGetChapter():
            sauce = request.get('{}'.format(urlCh), verify=False) # to do get the link
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
            testAgent = self.url # false
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
            # get the chapter input
            start = link.rfind('c')+1
            end = link.rfind('/')
            numberchapt = link[start:end]
            for x in range(0, 2):
                if numberchapt[0] == '0':
                    numberchapt = numberchapt[1:]
            if int(numberchapt)<=self.chEnd and int(numberchapt)>=self.chStart:
                resultatChapter.append(link)     
        
            
        return resultatChapter
                    
    def  mangafoxGetAllPageChapter(self):
        #initiation of bs
        sauce = request.get(self.url, verify=False)
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
        return listNumberPage