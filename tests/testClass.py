import sys
sys.path.append(r'C:\Users\Utilisateur\Documents\Python_Scripts\webScraping\manga')

from mangaScraping import mangaFinder

test = mangaFinder('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/',1.0,3.0,r'C:\Users\Utilisateur\Documents\Livre\manga')
#print(test.mangafoxGetChapter())

#print(test.mangafoxGetAllPageChapter('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/c001/1.html'))
print(test.pageDownloaded)
for a in test.mangafoxDowload():
    print(test.pageDownloaded)
 
#print(test.mangafoxNameFolder('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/v05/c040/'))
#test.manageImage(1,'test')
#test.setVariable('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/',1,3,r'C:\Users\Utilisateur\Documents\Livre\manga')