
import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
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
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Mainpage, DNS):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is 2810 Assignment Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Main Page",
                            command=lambda: controller.show_frame("Mainpage"))
        button2 = tk.Button(self, text="Go to Date and School",
                            command=lambda: controller.show_frame("DNS"))
        button1.pack()
        button2.pack()


class Mainpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Main page ", font=controller.title_font)
        
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
                
        #self.winfo_geometry("2000x3000") #set size
        resultTree=ttk.Treeview(self,colum=data_header)


        def search():
            start=oop_main.basic_function(startYearvar.get(),startMonthvar.get(),endYearvar.get(),endMonthvar.get(),schoolZoneBool.get())
            oop_mainrangedate=start.get_date_range()
            if schoolZoneBool.get():
                testresult=(data[data['OFFENCE_MONTH'].between(oop_mainrangedate[0],oop_mainrangedate[-1])&(data['SCHOOL_ZONE_IND']=='Y')])#>=oop_mainrangedate[0])&(data['OFFENCE_MONTH']<=oop_mainrangedate[-1])
            else:

                testresult=(data[data['OFFENCE_MONTH'].between(oop_mainrangedate[0],oop_mainrangedate[-1])])#>=oop_mainrangedate[0])&(data['OFFENCE_MONTH']<=oop_mainrangedate[-1])
            showing_data=pd.DataFrame(testresult).to_numpy().tolist()
            for i in resultTree.get_children():
                resultTree.delete(i)
            #print(testresult)
            for row in showing_data:
                #print(row)
                resultTree.insert('', 'end', values = row)


        #generate title
        title=tk.Label(self,text="Display all the data from  NSW report")

        #generate dropdown box for year and month
        #+++++++++++++++++++++++++Start Month, Year++++++++++++++++++++++++++++++
        startYearLabel=tk.Label(self,text="Start Year: ")
        startMonthLabel=tk.Label(self,text="Start Month: ")

        startYearvar=StringVar()
        startYearCombobox=ttk.Combobox(self,textvariable=startYearvar)
        startYearCombobox['values']=year_range

        startMonthvar=StringVar()
        startMonthCombobox=ttk.Combobox(self,textvariable=startMonthvar)
        startMonthCombobox['values']=month_range

        #########################Stat date choose finish##############

        #########################end date choose finish##############

        endYearLabel=tk.Label(self,text="end Year: ")
        endMonthLabel=tk.Label(self,text="end Month: ")

        endYearvar=StringVar()
        endYearCombobox=ttk.Combobox(self,textvariable=endYearvar)
        endYearCombobox['values']=year_range
        endMonthvar=StringVar()
        endMonthCombobox=ttk.Combobox(self,textvariable=endMonthvar)
        endMonthCombobox['values']=month_range




        #########################end date choose finish##############


        #==============================School Zone============================

        schoolZoneBool=tk.BooleanVar()

        schoolZoneCheckbox=tk.Checkbutton(self,text="School Zone",variable=schoolZoneBool,onvalue=True,offvalue=False)
        #===============================School Zone End=============================






        searchbutton=tk.Button(self,text="search",command=search)

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
        width=self.winfo_screenmmwidth() #width of screen (page)

        title.place(x=width/2, y=0)#grid(column=0, row=1,padx=1, pady=10)
        startYearLabel.place(x=23, y=25)#grid(column=0,row=2,sticky='w',padx=1, pady=10)
        #+x60
        startYearCombobox.place(x=83, y=25)#grid(column=1, row=2,sticky='w',padx=1, pady=10) #column => x axis , row=>y axis
        #+x 170
        startMonthLabel.place(x=253, y=25)#grid(column=0,row=3,sticky='nsew')
        startMonthCombobox.place(x=313, y=25)#grid(column=3, row=2,sticky='nsew')
        
        endYearLabel.place(x=483, y=25)#grid(column=4,row=2,sticky='w')
        endYearCombobox.place(x=543, y=25)#grid(column=5,row=2,sticky='w')
        
        endMonthLabel.place(x=713, y=25)#grid(column=6,row=2,sticky='w')
        endMonthCombobox.place(x=773, y=25)#grid(column=7,row=2,sticky='w')
        
        schoolZoneCheckbox.place(x=943, y=25)#grid(column=8,row=2,sticky='w')
        searchbutton.place(x=1003, y=25)#grid(column=9,row=2,sticky='w')
        resultTree.place(x=0, y=55)#grid(column=0,row=4,columnspan=10,sticky='nsew')
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.place(x=0, y=0)#grid(row=0,column=10)
        

class DNS(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Main page ", font=controller.title_font)
        
        
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
                
        #self.winfo_geometry("2000x3000") #set size
        resultTree=ttk.Treeview(self,colum=data_header)


        def search():
            start=oop_main.basic_function(startYearvar.get(),startMonthvar.get(),endYearvar.get(),endMonthvar.get(),schoolZoneBool.get())
            oop_mainrangedate=start.date_and_school()
            fig = Figure(figsize = (20, 5),dpi = 100)
            ax=fig.add_subplot(111)
            chart_type=FigureCanvasTkAgg(fig,self)
            chart_type.get_tk_widget().place(x=0, y=55)
            

        #generate title
        title=tk.Label(self,text="Display all the data from  NSW report")

        #generate dropdown box for year and month
        #+++++++++++++++++++++++++Start Month, Year++++++++++++++++++++++++++++++
        startYearLabel=tk.Label(self,text="Start Year: ")
        startMonthLabel=tk.Label(self,text="Start Month: ")

        startYearvar=StringVar()
        startYearCombobox=ttk.Combobox(self,textvariable=startYearvar)
        startYearCombobox['values']=year_range

        startMonthvar=StringVar()
        startMonthCombobox=ttk.Combobox(self,textvariable=startMonthvar)
        startMonthCombobox['values']=month_range

        #########################Stat date choose finish##############

        #########################end date choose finish##############

        endYearLabel=tk.Label(self,text="end Year: ")
        endMonthLabel=tk.Label(self,text="end Month: ")

        endYearvar=StringVar()
        endYearCombobox=ttk.Combobox(self,textvariable=endYearvar)
        endYearCombobox['values']=year_range
        endMonthvar=StringVar()
        endMonthCombobox=ttk.Combobox(self,textvariable=endMonthvar)
        endMonthCombobox['values']=month_range




        #########################end date choose finish##############


        #==============================School Zone============================

        schoolZoneBool=tk.BooleanVar()

        schoolZoneCheckbox=tk.Checkbutton(self,text="School Zone",variable=schoolZoneBool,onvalue=True,offvalue=False)
        #===============================School Zone End=============================






        searchbutton=tk.Button(self,text="search",command=search)

        #==========================Present List and show======================

        


        #===========================end=========================



        #positioning =================================
        width=self.winfo_screenmmwidth() #width of screen (page)

        title.place(x=width/2, y=0)#grid(column=0, row=1,padx=1, pady=10)
        startYearLabel.place(x=23, y=25)#grid(column=0,row=2,sticky='w',padx=1, pady=10)
        #+x60
        startYearCombobox.place(x=83, y=25)#grid(column=1, row=2,sticky='w',padx=1, pady=10) #column => x axis , row=>y axis
        #+x 170
        startMonthLabel.place(x=253, y=25)#grid(column=0,row=3,sticky='nsew')
        startMonthCombobox.place(x=313, y=25)#grid(column=3, row=2,sticky='nsew')
        
        endYearLabel.place(x=483, y=25)#grid(column=4,row=2,sticky='w')
        endYearCombobox.place(x=543, y=25)#grid(column=5,row=2,sticky='w')
        
        endMonthLabel.place(x=713, y=25)#grid(column=6,row=2,sticky='w')
        endMonthCombobox.place(x=773, y=25)#grid(column=7,row=2,sticky='w')
        
        schoolZoneCheckbox.place(x=943, y=25)#grid(column=8,row=2,sticky='w')
        searchbutton.place(x=1003, y=25)#grid(column=9,row=2,sticky='w')
        #resultTree.place(x=0, y=55)#grid(column=0,row=4,columnspan=10,sticky='nsew')
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.place(x=0, y=0)#grid(row=0,column=10)
        
       


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()