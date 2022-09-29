from calendar import month
from cgitb import reset
from datetime import datetime
from enum import unique
from itertools import count
from operator import truediv
from tracemalloc import start
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from draw_graph import *
import re


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


    def get_date_range(self):
        

        #inspired from https://stackoverflow.com/questions/5734438/how-to-create-a-month-iterator

        ym_start = 12*int(self.start_year)+int(self.start_month)-1
        ym_end = 12*int(self.end_year)+int(self.end_month)+1
        for ym in range(ym_start,ym_end):
            y,m=divmod(ym,12)
            self.range_date.append([y,m+1]) #year and month 
            #type(int) -> convert into string?
        #print(self.range_date)

        for i in range(len(self.range_date)):
            year=self.range_date[i][0]
            month=self.range_date[i][1]
            year=str(year)
            month=str(month)
            date_change='01-'+month+'-'+year #type string
            date_change=datetime.strptime(date_change, '%d-%m-%Y').strftime('%d/%m/%Y')
            self.range_date_date_format.append(date_change)


    def date_and_school(self):
        result=0

        self.get_date_range()



        data=pandas.read_csv('data.csv')
        data['OFFENCE_MONTH']=pandas.to_datetime(data['OFFENCE_MONTH'])

        data=pd.DataFrame(data)
        #print(data[data["OFFENCE_MONTH"]==self.range_date_date_format[0]].count())
        if self.school_zone_bool==True:
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                count=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['SCHOOL_ZONE_IND']=='Y')]).count()['OFFENCE_MONTH']
                self.month_result[self.range_date_date_format[i]]=count
        else:
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                count=pd.DataFrame(data[data['OFFENCE_MONTH']==self.range_date_date_format[i]]).count()['OFFENCE_MONTH']
                self.month_result[self.range_date_date_format[i]]=count
        
        #sort the dictionary

        test_oop=draw_graph(self.month_result)
        bar_graph=test_oop.draw_bar_graph()
        line_graph=test_oop.draw_line_graph()
        double_line_graph=test_oop.draw_2_line_graph()
        pie_chart=test_oop.draw_pie_chart()
    def camera_or_radar(self):
        result=0
        camera_result={} #SPEED_CAMERA_IND #Camera recorded in block D
        radar_result={} #'Radar' -- section h=='Y'
        self.get_date_range()
    

        data=pandas.read_csv('data.csv')
        data['OFFENCE_MONTH']=pandas.to_datetime(data['OFFENCE_MONTH'])
        data=pd.DataFrame(data)

        

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
        print(radar_result)
        print(camera_result)
        #-------------------------------------------------------------------------------------------------------------------------
        test_oop=draw_graph(self.month_result)
        double_line_graph=test_oop.draw_2_line_graph(radar_result,camera_result)


    def distribution_of_offence_code(self):
        result=0
        unique_Offence_code_count={}
        self.get_date_range()
        result={}
        final_result={}
        data=pandas.read_csv('data.csv')
        data['OFFENCE_MONTH']=pandas.to_datetime(data['OFFENCE_MONTH'])
        data=pd.DataFrame(data)
        unique_Offence_code=list(data['OFFENCE_CODE'].unique())
        
        start_date=self.range_date_date_format[0]
        end_date=self.range_date_date_format[-1]
        if self.school_zone_bool==True:
            data=pd.DataFrame(data[data['SCHOOL_ZONE_IND']=='Y'])

            data=data[data['OFFENCE_MONTH'].between(start_date,end_date)]
            #print(data.groupby('OFFENCE_CODE')['OFFENCE_DESC'].count().reset_index(name='OFFENCE_DESC').sort_values(['OFFENCE_DESC'],ascending=False).head(5))
            test1=data.groupby('OFFENCE_DESC').size().sort_values(ascending=False)
            test1=test1.iloc[0:5].to_dict()
            print(test1)
        else:
            data=data[data['OFFENCE_MONTH'].between(start_date,end_date)]
            #print(data.groupby('OFFENCE_CODE')['OFFENCE_DESC'].count().reset_index(name='OFFENCE_DESC').sort_values(['OFFENCE_DESC'],ascending=False).head(5))
            test1=data.groupby('OFFENCE_DESC').size().sort_values(ascending=False) #if want offence code only then change 'OFFFENCE_DESC' into 'OFFENCE_CODE'
            test1=test1.iloc[0:5].to_dict()
            #print(test1)
        test_oop=draw_graph(self.month_result)
        double_line_graph=test_oop.draw_pie_chart(test1,start_date,end_date)




        #group by Offence_code
        #---------------------------------------------------------------------------------
        # offence_code_top_5=list(test1.keys())
        # offence_code_value_5=list(test1.values())
        # for i in range(len(offence_code_top_5)):
        #     #print(offence_code_top_5[i])
        #     print(offence_code_value_5[i])
        #     offence_desc=data.loc[data['OFFENCE_CODE']==offence_code_top_5[i]]
        #     offence_desc=offence_desc['OFFENCE_DESC'].iloc[0]
        #     print(offence_desc)
        #     final_result[offence_desc]=offence_code_value_5[i]
        # print(final_result.values())
    def mobile_phone_usage(self):
        print('something')

start=basic_function('2012','01','2017','02',False)
test = start.camera_or_radar()


#https://www.entechin.com/how-to-import-a-class-from-another-file-in-python/ -> how to use other file class in OOP