import sys 
import bs4 as bs
import requests as request
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
        
def testDowload():

    url  ='http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/v01/c001/1.html'
    sauce = request.get(url, verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    
    end = url.find('html')-1
    start = url.rfind('/')+1
    fileName = url[start:end]
    print(fileName)
    
    allresult = soup.find_all('img')
    stringResult = str(allresult[0])
    
    start = stringResult.find('src=')
    urlImage = stringResult[start:]
    end = urlImage.find(' ')-1
    urlImage = urlImage[5:end]
    urlImage = urlImage.replace('amp;','')
    
    
    print(urlImage)
    
    img_data = request.get(urlImage).content
    with open('{}.jpg'.format(fileName), 'wb') as handler:
        handler.write(img_data)
def testGetChapter():
    
    url  ='http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/'
    sauce = request.get(url, verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    allResult = soup.find_all('a')
    resultatChapter = []
    temp = []
    for result in allResult:
        testAgent = '//mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/'
        testAgent2 = 'title'
        
        if  testAgent in str(result) and testAgent2 in str(result):
            pass
        else:
            temp.append(result)
    
    for el in temp:
        allResult.remove(el)
    inf= 25
    sup = 40       
    for result in allResult:
        start = str(result).find('href="') +6
        end = str(result).find('" title')
        link = 'https:'+str(result)[start:end]
        
        start = link.rfind('c')+1
        end = link.rfind('/')
        numberchapt = link[start:end]
        for x in range(0, 2):
            if numberchapt[0] == '0':
                numberchapt = numberchapt[1:]
        if int(numberchapt)<=sup and int(numberchapt)>=inf:
            resultatChapter.append(link)     
        
        
        
    print(resultatChapter)
 
def testGetAllPage():
    url  ='http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/c001/1.html'
    sauce = request.get(url, verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    
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
    listUrlPage = []
    
        
testGetChapter()
