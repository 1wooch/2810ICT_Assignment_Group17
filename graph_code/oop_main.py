from calendar import month
from cgitb import reset
from datetime import datetime
from enum import unique
from fileinput import filename
from genericpath import isfile
from itertools import count
from operator import truediv
from tracemalloc import start
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from draw_graph_all import draw_graph
import re
import os.path
#from oop_main_test import *

class basic_function(object):
    def __init__(self,start_year,start_month,end_year,end_month,school_zone_bool):
        self.start_year = start_year
        self.start_month=start_month
        self.end_year = end_year
        self.end_month = end_month
        self.school_zone_bool = school_zone_bool
        self.range_date=[]
        self.range_date_date_format=[]
        self.month_result={}
        self.filename='graph_code\data.csv'
       
#inspired from https://stackoverflow.com/questions/5734438/how-to-create-a-month-iterator
    


    def readDataFile(self,filename):
        if os.path.isfile(filename):
            data=pd.read_csv(filename)
            data['OFFENCE_MONTH']=pd.to_datetime(data['OFFENCE_MONTH'])
            data=pd.DataFrame(data)
            return data
        else:
            return "file not exist"




    def get_date_range(self):
        if self.start_month.isdigit()==False:
            return "Start Month is wrong"

        elif self.start_year.isdigit()==False:
            return "Start year is wrong"
        elif self.end_month.isdigit()==False:
            return "end Month is wrong"
        elif self.end_year.isdigit()==False:
            return "end year is wrong"
        elif int(self.start_month)+int(self.start_year)>int(self.end_month)+int(self.end_year):
            return "end year can not before start date"

        else:
            ym_start = 12*int(self.start_year)+int(self.start_month)-1
            ym_end = 12*int(self.end_year)+int(self.end_month)
            for ym in range(ym_start,ym_end):
                y,m=divmod(ym,12)
                self.range_date.append([y,m+1]) #year and month 


            for i in range(len(self.range_date)):
                year=self.range_date[i][0]
                month=self.range_date[i][1]
                year=str(year)
                month=str(month)
                date_change='01-'+month+'-'+year #type string
                date_change=datetime.strptime(date_change, '%d-%m-%Y').strftime('%d/%m/%Y')
                self.range_date_date_format.append(date_change)

            return self.range_date_date_format

    def date_and_school(self): #basic universial result.
        data=self.readDataFile(self.filename)
        range_date=self.get_date_range()


        start_date=self.range_date_date_format[0]
        end_date=self.range_date_date_format[-1]
        
        if(isinstance(range_date,list)):
            #print(data[data["OFFENCE_MONTH"]==self.range_date_date_format[0]].count())
            if self.school_zone_bool==True:
                for i in range(len(self.range_date_date_format)):
                    month=self.range_date_date_format[i]
                    count=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['SCHOOL_ZONE_IND']=='Y')]).count()['OFFENCE_MONTH']
                    self.month_result[self.range_date_date_format[i]]=count
                return self.month_result,start_date,end_date,'Traffic Penelty Record in School Zone'


            else:
                for i in range(len(self.range_date_date_format)):
                    month=self.range_date_date_format[i]
                    count=pd.DataFrame(data[data['OFFENCE_MONTH']==month]).count()['OFFENCE_MONTH']
                    self.month_result[self.range_date_date_format[i]]=count

                return self.month_result,start_date,end_date,'Traffic Penelty Record'
        
            #sort the dictionary
            #test_oop=draw_graph(self.month_result)
            #bar_graph=test_oop.draw_bar_graph()
        else:
            print(range_date)
       

    def camera_or_radar(self): #change into generate 2 plot 
        result=0 
        camera_result={} #SPEED_CAMERA_IND #Camera recorded in block D
        radar_result={} #'Radar' -- section h=='Y'
        range_date = self.get_date_range()

        data=self.readDataFile(self.filename) 
        if(isinstance(range_date,list)):

            #------------------------------------------------------------------------------------------------------------------------
            #Camera found
            #------------------------------------------------------------------------------------------------------------------------
            if self.school_zone_bool==True:
                for i in range(len(self.range_date_date_format)):
                    count=0
                    month=self.range_date_date_format[i]

                    basic_data=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['SCHOOL_ZONE_IND']=='Y')])
                    for j in range(len(basic_data)):
                        if(re.search("-\sCamera",str(basic_data['OFFENCE_DESC'].iloc[j]))):
                            count+=1
                    camera_result[self.range_date_date_format[i]]=count
            else:
                for i in range(len(self.range_date_date_format)):
                    count=0
                    month=self.range_date_date_format[i]
                    basic_data=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])])
                    for j in range(len(basic_data)):
                        if(re.search("-\sCamera",str(basic_data['OFFENCE_DESC'].iloc[j]))):
                            count+=1
                    camera_result[self.range_date_date_format[i]]=count
            #-------------------------------------------------------------------------------------------------------------------------
            # Radar found
            #-------------------------------------------------------------------------------------------------------------------------
            if self.school_zone_bool==True:
                for i in range(len(self.range_date_date_format)):
                    count=0
                    month=self.range_date_date_format[i]
                    basic_data=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['SCHOOL_ZONE_IND']=='Y')])
                    for j in range(len(basic_data)):
                        if(re.search("-\sRadar",str(basic_data['OFFENCE_DESC'].iloc[j]))):
                            count+=1
                    radar_result[self.range_date_date_format[i]]=count
            else:
                for i in range(len(self.range_date_date_format)):
                    count=0
                    month=self.range_date_date_format[i]
                    basic_data=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])])
                    for j in range(len(basic_data)):
                        if(re.search("-\sRadar",str(basic_data['OFFENCE_DESC'].iloc[j]))):
                            count+=1
                    radar_result[self.range_date_date_format[i]]=count

            #-------------------------------------------------------------------------------------------------------------------------
            test_oop=draw_graph(self.month_result)
            start_date=self.range_date_date_format[0]
            end_date=self.range_date_date_format[-1]
            double_line_graph=test_oop.draw_2_line_graph(radar_result,camera_result,start_date,end_date)
        else:
            return range_date

    def distribution_of_offence_code(self):
        result=0
        unique_Offence_code_count={}
        range_date= self.get_date_range()
        result={}
        final_result={}
        data=self.readDataFile(self.filename)
        if(isinstance(range_date,list)):
            print(data)
            unique_Offence_code=list(data['OFFENCE_CODE'].unique())
            
            start_date=self.range_date_date_format[0]
            end_date=self.range_date_date_format[-1]
            if self.school_zone_bool==True:
                data=pd.DataFrame(data[data['SCHOOL_ZONE_IND']=='Y'])

                data=data[data['OFFENCE_MONTH'].between(start_date,end_date)]
                test1=data.groupby('OFFENCE_DESC').size().sort_values(ascending=False)
                test1=test1.iloc[0:5].to_dict()
            else:
                data=data[data['OFFENCE_MONTH'].between(start_date,end_date)]
                test1=data.groupby('OFFENCE_DESC').size().sort_values(ascending=False) #if want offence code only then change 'OFFFENCE_DESC' into 'OFFENCE_CODE'
                test1=test1.iloc[0:5].to_dict()
            test_oop=draw_graph(self.month_result)
            #draw_pie_chart=test_oop.draw_pie_chart(test1,start_date,end_date,'Distribution of Offence Code')
            return test1,start_date,end_date,'Distribution of Offence Code'
        else:
            return range_date
   
    
##=============start oop_main.py================
start=basic_function('2012','01','2017','02',True)
#result = start.date_and_school() #running test
##===============start draw graph py
data=start.date_and_school()
test_oop=draw_graph(start.month_result)
draw_bar=test_oop.draw_line_graph(data[1],data[2],data[3])
##===============================================
##====================set data for offence code
#data=start.distribution_of_offence_code()
##==================================================
##-=========================put data in pie chart
#bar_graph=test_oop.draw_pie_chart(data[0],data[1],data[2],data[3])
##=====================================================

##================for double line graph===================
#lines=start.camera_or_radar()
##======================================================
#https://www.entechin.com/how-to-import-a-class-from-another-file-in-python/ -> how to use other file class in OOP