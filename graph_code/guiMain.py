import tkinter as tk
from unittest import result

from matplotlib.pyplot import title
from pyparsing import col
import oop_main
import pandas as pd
import datetime
from tkinter import Scrollbar, StringVar, ttk
from tkinter.messagebox import showinfo
from datetime import datetime










data = pd.read_csv("penalty_data_set_2.csv")
data['OFFENCE_MONTH']=pd.to_datetime(data['OFFENCE_MONTH'])

data=pd.DataFrame(data)
data_rows=data.to_numpy().tolist() 
data_header=data.columns.tolist() #get header
showing_data=data_rows[:30]
#+++++++++++++++++++++Get latest and oldest date+++++++++++++++++++++++++++++++++++++
latest_date=data['OFFENCE_MONTH'].max()
least_date=data['OFFENCE_MONTH'].min()
leastYear=2012
latestYear=2016
choosen_startYear=""
choosen_startMonth=""
choosen_endYear=""
choosen_endMonth=""







year_range=[] #-> add all of the year between oldest year to latest year on data set
for i in range(leastYear,latestYear+1):
    year_range.append(i)
month_range=['1','2','3','4','5','6','7','8','9','10','11','12']
#========================================================================

# start gui==========================================
mainpagegui=tk.Tk()
mainpagegui.geometry("2000x3000") #set size
resultTree=ttk.Treeview(mainpagegui,colum=data_header)


def search():
    start=oop_main.basic_function(startYearvar.get(),startMonthvar.get(),endYearvar.get(),endMonthvar.get(),schoolZoneBool.get())
    oop_mainrangedate=start.get_date_range()
    testresult=(data[data['OFFENCE_MONTH'].between(oop_mainrangedate[0],oop_mainrangedate[-1])])#>=oop_mainrangedate[0])&(data['OFFENCE_MONTH']<=oop_mainrangedate[-1])


    showing_data=pd.DataFrame(testresult).to_numpy().tolist()

    for i in resultTree.get_children():
        resultTree.delete(i)
    #print(testresult)
    for row in showing_data:
        #print(row)
        resultTree.insert('', 'end', values = row)


#generate title
title=tk.Label(mainpagegui,text="Display all the data from  NSW report")

#generate dropdown box for year and month
#+++++++++++++++++++++++++Start Month, Year++++++++++++++++++++++++++++++
startYearLabel=tk.Label(mainpagegui,text="Start Year: ")
startMonthLabel=tk.Label(mainpagegui,text="Start Month: ")

startYearvar=StringVar()
startYearCombobox=ttk.Combobox(mainpagegui,textvariable=startYearvar)
startYearCombobox['values']=year_range

startMonthvar=StringVar()
startMonthCombobox=ttk.Combobox(mainpagegui,textvariable=startMonthvar)
startMonthCombobox['values']=month_range

#########################Stat date choose finish##############

#########################end date choose finish##############

endYearLabel=tk.Label(mainpagegui,text="end Year: ")
endMonthLabel=tk.Label(mainpagegui,text="end Month: ")

endYearvar=StringVar()
endYearCombobox=ttk.Combobox(mainpagegui,textvariable=endYearvar)
endYearCombobox['values']=year_range
endMonthvar=StringVar()
endMonthCombobox=ttk.Combobox(mainpagegui,textvariable=endMonthvar)
endMonthCombobox['values']=month_range




#########################end date choose finish##############


#==============================School Zone============================

schoolZoneBool=tk.BooleanVar()

schoolZoneCheckbox=tk.Checkbutton(mainpagegui,text="School Zone",variable=schoolZoneBool,onvalue=True,offvalue=False)
#===============================School Zone End=============================






searchbutton=tk.Button(mainpagegui,text="search",command=search)

#==========================Present List and show======================

resultTree.column('#0', width = 1)

for label in resultTree['column']:
    resultTree.heading(label,text=label)

for row in showing_data:
    resultTree.insert('', 'end', values = row)#input data in result tree

def item_selected(event): #if user click the row
    for selected_item in resultTree.selection():
        item=resultTree.item(selected_item)
        record=item['values']
        showinfo(title="Information",message=','.join(record))

resultTree.bind('<<TreeviewSelect>>', item_selected)



#===========================end=========================



#positioning =================================
width=mainpagegui.winfo_screenmmwidth() #width of screen (page)

title.grid(column=0, row=1)
startYearLabel.grid(column=0,row=2,sticky='w')
startYearCombobox.grid(column=1, row=2,sticky='w') #column => x axis , row=>y axis
startMonthLabel.grid(column=2,row=2,sticky='w')
startMonthCombobox.grid(column=3, row=2,sticky='w')
endYearLabel.grid(column=4,row=2,sticky='w')
endYearCombobox.grid(column=5,row=2,sticky='w')
endMonthLabel.grid(column=6,row=2,sticky='w')
endMonthCombobox.grid(column=7,row=2,sticky='w')
schoolZoneCheckbox.grid(column=8,row=2,sticky='w')
searchbutton.grid(column=9,row=2,sticky='w')
resultTree.grid(column=0,row=4,columnspan=10,sticky='nsew')
mainpagegui.grid_rowconfigure(4,weight=1)
mainpagegui.grid_columnconfigure(1,weight=1) #ce


mainpagegui.mainloop()
