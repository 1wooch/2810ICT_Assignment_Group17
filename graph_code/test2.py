from oop_main import *
from datetime import datetime
import unittest

class testFile(unittest.TestCase):
    def testFile(self):
        oopmain=basic_function('2012','01','2017','02',False)
        print(oopmain.readDataFile('data.txt'))
        self.assertEqual(oopmain.readDataFile('data.txt'),"file not exist")
     
 #coverage tool =>html? morethan 80%
 #10-12 test
if __name__=='__main__':
    unittest.main()