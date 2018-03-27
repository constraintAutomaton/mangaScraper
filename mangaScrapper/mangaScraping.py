import sys
import bs4 as bs
import requests as request
import time
import os


class mangaFinder():
    def __init__(self, url='', start=0.0, end=0.0, folder=os.getcwd()):
        try:
            self.url = url
            self.chStart = start
            self.chEnd = end
            self.domain = self.url[:self.url.find('.')]
            self.folder = folder
            self.folderActive = []
            self.totalPage = 0
            self.pageDownloaded = 0
            

            # Error handling

            if not (isinstance(self.url, str)):
                raise TypeError('The url have to be a string')

            elif not (isinstance(self.chEnd, float)) and not (isinstance(
                    self.chStart, float)):

                raise TypeError(
                    'The start and ending chapter have to be number')

            elif not (os.path.isdir(r'{}'.format(folder))):
                raise ValueError("The directory don't exist")

            elif self.chStart > self.chEnd:

                raise ValueError(
                    'The ending chapter have to be after the start chapter')

        except TypeError as error:  # maybe find a way to catch the error in one line

            print(repr(error))

        except ValueError as error:

            print(repr(error))

    def mangafoxDownload(self):
        try:
            if self.domain == 'http://fanfox':
                pass
            else:
                raise ValueError(
                    'Url not valid for the moment we only support manga fox ')
        except ValueError as error:

            print(repr(error))

        self.totalPage = 0
        self.pageDownloaded = 0
        self.folderActive = []

        allChapt = self.mangafoxGetChapter(
        )  # get all the chapters ask by the user
        self.mangafoxGetTotalPage(allChapt)

        for urlCh in allChapt:
            # create the folder of the chapter
            try:
                folder = self.mangafoxNameFolder(urlCh)
                os.makedirs(os.path.join(self.folder,folder))
                self.folderActive.append(os.path.join(self.folder,folder))
            except:
                pass

            allPage = self.mangafoxGetAllPageChapter(
                urlCh)  # get all the page of the user

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

                end = urlPage.find('html') - 1
                start = urlPage.rfind('/') + 1
                fileName = urlPage[start:end]
                # name of the jpg file

                result = soup.find('img')
                stringResult = str(result)

                # find the tag whit the link of the image
                start = stringResult.find('src=')
                urlImage = stringResult[start:]
                end = urlImage.find(' ') - 1
                urlImage = urlImage[5:end]
                urlImage = urlImage.replace('amp;', '')
                # get the link of the image by delete the 'junk text' of the tag

                if not (os.path.isfile(os.path.join(self.folder,folder,fileName))):
                    img_data = request.get(urlImage).content
                    with open('{}.jpg'.format(fileName), 'wb') as handler:
                        handler.write(img_data)
                    self.manageImage(fileName, folder)
                else:
                    pass

                self.pageDownloaded += 1
                yield self.pageDownloaded

                # dowload the image

    def mangafoxGetChapter(self):
        # initiation of bs
        sauce = ''
        while sauce == '':
            try:
                sauce = request.get(self.url, verify=False)
            except:
                time.sleep(5)

                continue

        soup = bs.BeautifulSoup(sauce.text, 'html.parser')
        allResult = soup.find_all('a')

        resultatChapter = []  # list of chapter

        temp = []  # list of tag whitout the chapter
        # get tag whit chapter
        for result in allResult:
            testAgent = self.url[5:]  # false
            testAgent2 = 'title'

            if testAgent in str(result) and testAgent2 in str(result):
                pass
            else:
                temp.append(result)
        # delete the tag whiout the chapter
        for el in temp:
            allResult.remove(el)
        # extract the link out of the tag
        for result in allResult:
            start = str(result).find('href="') + 6
            end = str(result).find('" title')
            link = 'http:' + str(result)[start:end]
            # get the chapter input
            start = link.rfind('c') + 1
            end = link.rfind('/')
            numberchapt = link[start:end]
            for x in range(0, 2):
                if numberchapt[0] == '0':
                    numberchapt = numberchapt[1:]
            if float(numberchapt) <= self.chEnd and float(
                    numberchapt) >= self.chStart:
                resultatChapter.append(link)

        resultatChapter.reverse()
        return resultatChapter

    def mangafoxGetAllPageChapter(self, chapterUrl):

        # initiation of bs
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

        # find select tag who contains the text of the page of the chapter
        allResult = soup.find_all('select')

        tagNumberPage = str(allResult[1])

        start = find_nth(tagNumberPage, 'value="', 2, 'r') + 7
        end = tagNumberPage.find('"', start)
        numberPage = int(tagNumberPage[start:end])
        listNumberPage = []

        while numberPage > 0:
            listNumberPage.append(numberPage)
            numberPage -= 1
        listNumberPage.reverse()
        listPageUrl = []

        for page in listNumberPage:
            end = chapterUrl.rfind('/') + 1
            urlPage = chapterUrl[0:end] + str(page) + '.html'
            listPageUrl.append(urlPage)

        return listPageUrl

    def mangafoxNameFolder(self, urlCh):
        start = find_nth(urlCh, '/', 4, 'r') + 1
        name = urlCh[start:]
        loopName = name  # can't loop and modify

        for caracter in loopName:

            if caracter == '_' or caracter == '/':

                name = name.replace(caracter, ' ')
        name = name.replace(' 1.html', '')
        return name

    def mangafoxGetTotalPage(self, allChapter):

        # get the number of pages of all the chapter the user wants to download
        for chapter in allChapter:
            self.totalPage += len(self.mangafoxGetAllPageChapter(chapter))

    def mangafoxGetTitle(self, url):
        start = find_nth(url, '/', 4) + 1
        end = len(url)
        Title = url[start:end - 1]
        return Title

    def manageImage(self, image, folder):

        os.rename(r'{}.jpg'.format(image), os.path.join(self.folder,folder,image))

    def set_variable(self, url, start, end, folder):
        self.__init__(url, start, end, folder)
    def restart(self):
        self.__init__()


def find_nth(string, substring, nb, direction='f'):
    # find the position of the nth occurence of a substring
    if nb<1 :
        raise TypeError('number of iteration must be positive')
    elif nb>len(string):
        raise ValueError('the number of iteration must be lesser than the number of caracter')
    beg = string.find(substring)
    if beg == -1: 
        raise ValueError('substring not in string')
    past = None
    if direction == 'f':
        while nb > 1 and beg < len(string):
            beg = string.find(substring, beg + 1)
            if beg==past:
                raise ValueError('the string countain less iteration of the substring. There \
                is {} iteration'.format(nb))
            nb -= 1
            past = beg
    else:
        result = [beg]
        while True:
            beg = string.find(substring, beg + 1)
            if beg==past:
                raise ValueError('the string countain less iteration of the substring. There \
                is {} iteration'.format(len(result)))
            result.append(beg)
            if result[len(result) - 1] == -1:
                break
            past = beg
        beg = result[len(result) - nb - 1]
    result = beg
    return result
