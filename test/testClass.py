from mangaScraping import mangaFinder

test = mangaFinder('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/',1,3,r'C:\Users\Utilisateur\Documents\Livre\manga')
#print(test.mangafoxGetChapter())

#print(test.mangafoxGetAllPageChapter('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/c001/1.html'))

#test.domainSplitter()
#print(test.mangafoxNameFolder('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/v05/c040/'))
#test.manageImage(1,'test')
test.setVariable('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/',1,3,r'C:\Users\Utilisateur\Documents\Livre\manga')