# coding: utf-8
import sys
import unittest
from unittest.mock import patch
sys.path.append(r'C:\Users\Utilisateur\Documents\Python_Scripts\webScraping\manga\mangaScrapper')
from mangaScraping import mangaFinder
from mangaScraping import find_nth
class mangaScrapping_test(unittest.TestCase):
    
    def setUp(self):
        self.mangaScrapper_1  = mangaFinder(url='http://mangafox.la/manga/tales_of_demons_and_gods/',
                                            start = 1.0,end=2.0)
        self.mangaScrapper_2  = mangaFinder(url='http://mangafox.la/manga/the_gamer/',start =5,end=6)
    def test_find_nth(self):
        string = 'I test my function test1, test2, test3'
     
        self.assertEqual(find_nth(string,'test',1),2)
        self.assertEqual(find_nth(string,'test',2),19)
        self.assertRaises(ValueError,lambda: find_nth(string,'test',100))
        
        self.assertEqual(find_nth(string,'test',1,direction='b'),33)
        self.assertEqual(find_nth(string,'test',2,direction='b'),26)
        self.assertRaises(ValueError,lambda: find_nth(string,'test',100,direction='b'))
        
        self.assertRaises(ValueError,lambda: find_nth(string,'missing',1))
        self.assertRaises(ValueError,lambda: find_nth(string,'missing',1,direction='b'))
        
if __name__ == '__main__':
    unittest.main()
        