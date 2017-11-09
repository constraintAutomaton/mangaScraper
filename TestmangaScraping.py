import sys 
import bs4 as bs
import requests as request
def testDowload():

    url  ='https://mangafox.me/manga/kobayashi_san_chi_no_maid_dragon/v01/c001/2.html'
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
    url  ='https://mangafox.me/manga/kobayashi_san_chi_no_maid_dragon/'
    sauce = request.get(url, verify=False)
    soup = bs.BeautifulSoup(sauce.text, 'html.parser')
    allResult = soup.find_all('a')
    
    temp = []
    for result in allResult:
        testAgent = '//mangafox.me/manga/kobayashi_san_chi_no_maid_dragon/'
        
        if  testAgent in str(result):
            pass
        else:
            temp.append(result)
    #print(temp)
    for el in temp:
        allResult.remove(el)
    print(allResult)

   
testGetChapter()