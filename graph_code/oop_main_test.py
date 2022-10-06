from datetime import datetime
import unittest
from unittest import result


class oop_main_test(unittest.TestCase):
    def __init__(self,result_list):
        self.result_list=result_list
        self.startmonth=result_list['startmonth']
        self.startyear=result_list['startyear']
        self.endmonth=result_list['endmonth']
        self.endyear=result_list['endyear']
        self.schoolzone=result_list['schoolzone']
        self.filename=result_list['filename']
        self.rangedate=result_list['rangedate']

    def test_start_month(self):
        #print(self.result_list['startmonth'])
        self.assertTrue(self.startmonth.isdigit())
    def test_start_year(self):
        #print(self.result_list['startmonth'])
        self.assertTrue(self.startyear.isdigit())
    def test_end_month(self):
        #print(self.result_list['startmonth'])
        self.assertTrue(self.endmonth.isdigit())
    def test_end_year(self):
        #print(self.result_list['startmonth'])
        self.assertTrue(self.endyear.isdigit())
    def test_schoolZone_bool(self):
        #print(self.result_list['startmonth'])
        self.assertTrue(isinstance(self.schoolzone,bool))
    def test_rangedate_list(self):
    #print(self.result_list['startmonth'])
        self.assertTrue(isinstance(self.rangedate,list))
    def test_range_date_date_test(self):
        #print(self.result_list['startmonth'])
        for i in range(len(self.rangedate)):
            self.assertTrue(isinstance(variable,datetime.datetime))
if __name__=='__main__':
    unittest.main()


        