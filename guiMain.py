import tkinter as tk
from unittest import result

from matplotlib.pyplot import title
from pyparsing import col
import oop_main
import pandas as pd
import datetime
from tkinter import Scrollbar, StringVar, ttk
from tkinter.messagebox import showinfo










data = pd.read_csv("penalty_data_set_2.csv")
data=pd.DataFrame(data)
data_rows=data.to_numpy().tolist() 
data_header=data.columns.tolist() #get header
showing_data=data_rows[:30]
#+++++++++++++++++++++Get latest and oldest date+++++++++++++++++++++++++++++++++++++
latest_date=datetime.datetime.strptime(data['OFFENCE_MONTH'].max(),"%d/%m/%Y")
least_date=datetime.datetime.strptime(data['OFFENCE_MONTH'].min(),"%d/%m/%Y")
leastMonth=least_date.month
leastYear=least_date.year
latestMonth=latest_date.month
latestYear=latest_date.year

year_range=[] #-> add all of the year between oldest year to latest year on data set
for i in range(leastYear,latestYear+1):
    year_range.append(i)
month_range=['1','2','3','4','5','6','7','8','9','10','11','12']
#========================================================================

# start gui==========================================
mainpagegui=tk.Tk()
mainpagegui.geometry("2000x3000") #set size


def search(start_month,start_year,end_month,end_year):
    print(start_month)
    print(start_year)
    print(end_month)
    print(end_year)

#generate title
title=tk.Label(mainpagegui,text="Display all the data from  NSW report")
#widget.pack()

#generate dropdown box for year and month
#+++++++++++++++++++++++++Start Month, Year++++++++++++++++++++++++++++++
startYearLabel=tk.Label(mainpagegui,text="Start Year: ")
startMonthLabel=tk.Label(mainpagegui,text="Start Month: ")

Startyearboxclicked=tk.StringVar()
Startyearboxclicked.set(year_range[0])

Startyeardropbox=tk.OptionMenu(mainpagegui,Startyearboxclicked,*year_range)
#Startyeardropbox.pack()

Startmonthboxclicked=tk.StringVar()
Startmonthboxclicked.set(month_range[0])

Startmonthdropbox=tk.OptionMenu(mainpagegui,Startmonthboxclicked,*month_range)
#Startmonthdropbox.pack()


startYearvar=StringVar()
startYearCombobox=ttk.Combobox(mainpagegui,textvariable=startYearvar)
startYearCombobox['values']=year_range

#########################Stat date choose finish##############

#########################end date choose finish##############

endYearLabel=tk.Label(mainpagegui,text="end Year: ")
endMonthLabel=tk.Label(mainpagegui,text="end Month: ")


endyearboxclicked=tk.StringVar()
endyearboxclicked.set(year_range[0])
endyeardropbox=tk.OptionMenu(mainpagegui,endyearboxclicked,*year_range)


endtmonthboxclicked=tk.StringVar()
endtmonthboxclicked.set(month_range[0])
endmonthdropbox=tk.OptionMenu(mainpagegui,endtmonthboxclicked,*month_range)





#########################end date choose finish##############

#generate search button(submit)
searchButton=tk.Button(mainpagegui,text="search")
#==============================School Zone============================

schoolZoneBool=tk.BooleanVar()

schoolZoneCheckbox=tk.Checkbutton(mainpagegui,text="School Zone",onvalue=True,offvalue=False)
#===============================School Zone End=============================



#generate search button
searchbutton=tk.Button(mainpagegui,text="search",command=search(startYearvar.get(),Startyearboxclicked.get(),endtmonthboxclicked.get(),endyearboxclicked.get()))



#searchButton.pack()



#==========================Present List and show======================

#resultListBox=tk.Listbox(mainpagegui)

resultTree=ttk.Treeview(mainpagegui,colum=data_header)
#for i in data_header:
    #resultTree.heading(data_header[i],text=data_header[i])
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


scrollbar=ttk.Scrollbar(mainpagegui,orient=tk.VERTICAL,command=resultTree.yview)
#resultTree.configure(yscroll)


#===========================end=========================



#positioning =================================
width=mainpagegui.winfo_screenmmwidth() #width of screen (page)

title.grid(column=0, row=1)
startYearLabel.grid(column=0,row=2,sticky='w')
startYearCombobox.grid(column=1, row=2,sticky='w') #column => x axis , row=>y axis
startMonthLabel.grid(column=2,row=2,sticky='w')
Startmonthdropbox.grid(column=3, row=2,sticky='w')
endYearLabel.grid(column=4,row=2,sticky='w')
endyeardropbox.grid(column=5,row=2,sticky='w')
endMonthLabel.grid(column=6,row=2,sticky='w')
endmonthdropbox.grid(column=7,row=2,sticky='w')
schoolZoneCheckbox.grid(column=8,row=2,sticky='w')
searchButton.grid(column=9,row=2,sticky='w')
resultTree.grid(column=0,row=4,columnspan=10,sticky='nsew')
mainpagegui.grid_rowconfigure(4,weight=1)
mainpagegui.grid_columnconfigure(1,weight=1) #ce
# mainpagegui.grid_columnconfigure(0,weight=1) #ce
# mainpagegui.grid_columnconfigure(2,weight=1) #ce
# mainpagegui.grid_columnconfigure(3,weight=1) #ce
# mainpagegui.grid_columnconfigure(4,weight=1) #ce
# mainpagegui.grid_columnconfigure(5,weight=1) #ce
# mainpagegui.grid_columnconfigure(6,weight=1) #ce
# mainpagegui.grid_columnconfigure(7,weight=1) #ce
# mainpagegui.grid_columnconfigure(8,weight=1) #ce
# mainpagegui.grid_columnconfigure(9,weight=1) #ce
# mainpagegui.grid_columnconfigure(10,weight=1) #ce

#mainpagegui.grid_columnconfigure(1,weight=1) #ce

 


#widget3=tk.Text(root) #generate text
#widget3.pack()

#tbox(root) #gnerate listbox
#widget4.pack() #make it happen


mainpagegui.mainloop()
