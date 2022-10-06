from cgitb import reset
from datetime import datetime
from itertools import count
from operator import truediv
from tracemalloc import start
from unittest import result
import pandas
import matplotlib.pyplot as plt
import numpy as np
import sys



class draw_graph(object):
    def __init__(self,month_result):
        self.month_result=month_result
        
        
    
    def draw_bar_graph(self,start_date,end_date,title): #mobile phone , School Zone
        start_date=str(start_date)
        end_date=str(end_date)
        title=str(title)
        plt.figure(figsize=(20,3))
        #width:20,height:3
        plt.title(label='%s \n From %s to %s' %(title,start_date,end_date) )

        plt.bar(range(len(self.month_result)),list(self.month_result.values()),align='center',width=0.3)
        #set width.
        plt.xticks(range(len(self.month_result)),list(self.month_result.keys()))
        plt.show()
    def draw_line_graph(self,start_date,end_date,title):
        start_date=str(start_date)
        end_date=str(end_date)
        title=str(title)
        plt.figure(figsize=(20,3))  
        plt.title(label='%s \n From %s to %s' %(title,start_date,end_date) )

        labels=np.array(list(self.month_result.keys())) #month
        y=np.array(list(self.month_result.values())) #data
        plt.plot(labels,y,linestyle='-',marker='o')
        plt.show()
    def draw_2_line_graph(self,first_data,second_data,start_date,end_date): #for radar or camera
        
        start_date=str(start_date)
        end_date=str(end_date)
        plt.title(' Radar or Camera \n From %s to %s' %(start_date,end_date))
        labels=np.array(list(first_data.keys()))
        first_data=np.array(list(first_data.values())).astype(np.double)
        second_data=np.array(list(second_data.values())).astype(np.double)
        plt.plot(labels,first_data,linestyle='-',marker='o',label="Radar")
        plt.plot(labels,second_data,linestyle='-',marker='o',label="Camera")
        plt.legend(loc="upper left")
        plt.show()

    def draw_pie_chart(self,result_dictionary,start_date,end_date,title):
        explode = [0, 0, 0, 0.1, 0.3]
        start_date=str(start_date)
        end_date=str(end_date) 
        title=str(title)
        plt.title(label='%s \n From %s to %s' %(title,start_date,end_date) )
        #plt.title('From ',start_date,' to ',end_date)
        #self.month_result=sorted(self.month_result.items(),key=lambda x:x[1],reverse=True)
        #sort the dictionary

        label_list=list(result_dictionary.keys())
        data_list=list(result_dictionary.values())
        

        data=np.array(data_list)
        labels=np.array(label_list)
        plt.pie(data_list,labels=label_list,explode=explode)
        plt.show()



