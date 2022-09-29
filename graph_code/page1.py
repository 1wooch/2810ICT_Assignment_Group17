from cgitb import reset
from datetime import datetime
from itertools import count
from operator import index, truediv
from tracemalloc import start
import pandas
import matplotlib.pyplot as plt
import numpy as np
import sys


def q2(start_year,start_month,end_year,end_month,school_zone_bool):
    result=0
    range_date=[]

    #inspired from https://stackoverflow.com/questions/5734438/how-to-create-a-month-iterator

    ym_start = 12*int(start_year)+int(start_month)-1
    ym_end = 12*int(end_year)+int(end_month)-1
    for ym in range(ym_start,ym_end):
        y,m=divmod(ym,12)
        range_date.append([y,m+1]) #year and month 
        #type(int) -> convert into string?


   
        # start_date='01-'+self.start_month+'-'+self.start_year
        # start_date=datetime.strptime(start_date, '%d-%m-%Y').date()
        # end_date='01-'+self.end_month+'-'+self.end_year
        # end_date=datetime.strptime(end_date, '%d-%m-%Y').date()

        # for x in test.index:
        #     if (test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(start_date))&(test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(end_date)):
        #         if self.school_zone_bool==True:
        #             if test.loc[x,'SCHOOL_ZONE_IND']=='Y':
        #                 result+=1
        #         else:
        #             result+=1

    test=pandas.read_csv('data.csv')
    test['OFFENCE_MONTH']=pandas.to_datetime(test['OFFENCE_MONTH'])

    start_date='01-'+start_month+'-'+start_year
    start_date=datetime.strptime(start_date, '%d-%m-%Y').date()
    end_date='01-'+end_month+'-'+end_year
    end_date=datetime.strptime(end_date, '%d-%m-%Y').date()


    





    for x in test.index:
        if (test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(start_date))&(test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(end_date)):
            if school_zone_bool==True:
                if test.loc[x,'SCHOOL_ZONE_IND']=='Y':
                    result+=1
            else:
                result+=1


    print(range_date)
    print(result)


    xpoints = np.array([0,6])
    ypoints = np.array([0,result])
    plt.plot(xpoints,ypoints)
    plt.show()

q2('2012','01','2013','02',True)







# def q1(start_date,end_date,school_zone):
#     test=pandas.read_csv('data.csv')
#     #get a data from data.csv
#     test['OFFENCE_MONTH']=pandas.to_datetime(test['OFFENCE_MONTH'])
#     #convert OFFENCE_MONTH into date format.
#     start_date=datetime.strptime(start_date, '%m-%d-%Y').date()
#     #convert start date into date format.
#     count=0
#     count1=0
#     school_zone=0
#     #print(len(test.index)) #length of csv file?
#     for x in test.index:
#         if test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(start_date):
#             count+=1
#     for x in test.index:
#         if test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(end_date):
#             count1+=1
#     if school_zone==True:
#         for x in test.index: 
#             if test.loc[x,'SCHOOL_ZONE_IND']=='Y':
#                 school_zone+=1
    
   
#     xpoints = np.array([0,6])
#     ypoints = np.array([0,count])
#     plt.plot(xpoints,ypoints)
#     plt.show()
