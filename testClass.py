from mangaScraping import mangaFinder

test = mangaFinder('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/',1,2)
#print(test.mangafoxGetChapter())

#print(test.mangafoxGetAllPageChapter('http://mangafox.la/manga/kobayashi_san_chi_no_maid_dragon/c001/1.html'))

test.domainSplitter()