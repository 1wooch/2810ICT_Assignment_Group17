from oop_main import *
from datetime import datetime
import unittest

class testFile(unittest.TestCase):
    def testFile(self):
        oopmain=basic_function('2012','01','2017','02',False)
        self.assertEqual(oopmain.readDataFile('data.txt'),"file not exist")
    def testFileResultLength(self):
        oopmain=basic_function('2012','01','2017','02',False)
        self.assertEqual(len(oopmain.readDataFile('data.csv')),264608) #check the length of data is 264608 (all of the data load?)
    
    def test_get_date_range_result_check(self):
        oopmain=basic_function('2012','01','2017','02',False) # start year ,start month, end year , end month order
        self.assertIsInstance(oopmain.get_date_range(),list) #check the length of data is 264608 (all of the data load?)
    def test_get_date_type_check(self):
        oopmain=basic_function('2012','01','2017','02',False) # start year ,start month, end year , end month order
        test_value=oopmain.get_date_range()[0]
        print("test_get_date_value:",isinstance(test_value,datetime.date))
        #self.assertTrue(isinstance(test_value,datetime.date))


 
 
 #coverage tool =>html? morethan 80%
 #10-12 test
if __name__=='__main__':
    unittest.main()