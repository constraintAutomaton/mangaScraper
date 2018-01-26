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
        testFoward = find_nth(string,'test',1)
        testFoward_2 = find_nth(string,'test',2)
        testFoward_100 = find_nth(string,'test',100)
        
        testBackward = find_nth(string,'test',1,direction='b')
        testBackward_2 = find_nth(string,'test',2,direction='b')
        testBackward_100 = find_nth(string,'test',100,direction='b')        
        
        testFowardMissingForward = find_nth(string,'missing',1)
        testFowardMissingBackward = find_nth(string,'missing',1,direction='b')
        
        self.assertEqual(testFoward,2)
        self.assertEqual(testFoward_2,19)
        self.assertEqual(testFoward_100,33)
        
        self.assertEqual(testBackward,33)
        self.assertEqual(testBackward_2,26)
        self.assertEqual(testBackward_100,2)
        
        self.assertEqual(testFowardMissingForward,'')
        self.assertEqual(testFowardMissingBackward,'')
        
if __name__ == '__main__':
    unittest.main()
        