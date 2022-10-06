from oop_main import *
from datetime import date, datetime
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
        test_value=oopmain.get_date_range()
       
        self.assertTrue(test_value[0] is datetime.date) #-> fail it is string

    def test_get_date_type_length_check(self):
        oopmain=basic_function('2012','01','2012','02',False) # start year ,start month, end year , end month order
        #from 2012/Jan to 2012 / Feb -> range should be 2
        test_value=oopmain.get_date_range()
        self.assertEqual(len(test_value),2) #->pass

    def test_put_string_input_for_start_month(self):
        oopmain=basic_function('2012','abc','2012','02',False) # start year ,start month, end year , end month order
        #from 2012/Jan to 2012 / Feb -> range should be 2
        self.assertEqual(oopmain.get_date_range(),"Start Month is wrong")
    def test_put_string_input_for_start_year(self):
        oopmain=basic_function('20ab','01','2012','02',False) # start year ,start month, end year , end month order
        #from 2012/Jan to 2012 / Feb -> range should be 2
        self.assertEqual(oopmain.get_date_range(),"Start year is wrong")

    def test_put_string_input_for_end_year(self):
        oopmain=basic_function('2012','01','20ab','02',False) # start year ,start month, end year , end month order
        #from 2012/Jan to 2012 / Feb -> range should be 2
        self.assertEqual(oopmain.get_date_range(),"end year is wrong")

    def test_put_string_input_for_end_month(self):
        oopmain=basic_function('2012','01','2012','abcde',False) # start year ,start month, end year , end month order
        #from 2012/Jan to 2012 / Feb -> range should be 2
        self.assertEqual(oopmain.get_date_range(),"end Month is wrong")
    def test_put_string_input_for_start_year(self):
        oopmain=basic_function('2013','11','2012','02',False) # start year ,start month, end year , end month order
        #from 2012/Jan to 2012 / Feb -> range should be 2
        self.assertEqual(oopmain.get_date_range(),"end year can not before start date")
    
    def test_date_and_school_result(self):
        oopmain=basic_function('2013','11','2012','02',False) # start year ,start month, end year , end month order
        result=oopmain.date_and_school()
        self.assertFalse(isinstance(result,dict))  # because the end date is before start date the range_date will be error message so it should be false
    def test_date_and_school_result(self):
        oopmain=basic_function('2012','01','2012','11',False) # start year ,start month, end year , end month order
        result=oopmain.date_and_school()
        self.assertTrue(isinstance(result,dict))  # because the end date is before start date the range_date will be error message so it should be false



 #coverage tool =>html? morethan 80%
 #10-12 test
#if __name__=='__main__':
#    unittest.main()