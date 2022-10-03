from tkinter import *
from tkinter import ttk
import pandas as pd
import tkinter as tk

def filterTreeView(*args):
    ItemsOnTreeView = myTree.get_children()

    search = search_ent_var.get().capitalize()

    for eachItem in ItemsOnTreeView:
        if search in myTree.item(eachItem)['values'][2]:
            search_var = myTree.item(eachItem)['values']
            myTree.delete(eachItem)

            myTree.insert("", 0, value=search_var)

root = Tk()
root.title("NSW Traffic Penalty Data")

topFrame = Frame(root, bg="white")
topFrame.place(x=5, y=5, width=200, height=80)

treeFrame = Frame(root, bg="white")
treeFrame.place(x=5, y=100, width=1500, height=800)

lb1 = Label(topFrame, text="Search by", fg="black", bg="white")
lb1.grid(row=0, column=0)
search_ent_var = StringVar()
myentry = Entry(topFrame, textvariable=search_ent_var)
myentry.grid(row=0, column=1)
search_ent_var.trace("w", filterTreeView)

column = ['Financial Year', 'Month', 'Offence Code', 'Offence Description', 'Legislation', 'Section Clause',
          'Penalty Amount', 'Camera Offence', 'Camera Type', 'Camera Location', 'Camera Location Details', 'School Zone',
          'Speed Range', 'Speed Offence', 'Point to Point Offence', 'Red Light Camera Offence', 'Speed Camera Offence',
          'Seatbelt Offence', 'Mobile Phone Offence', 'Parking Offence', 'Criminal Infringement Notice Scheme Offence',
          'Food Safety Offence', 'Non-Motor Vehicle Offence', 'Number of Penalty Notices', 'Total Value of Penalty Notices']
data = pd.read_csv("penalty_data_set_2.csv")
data_rows = data.to_numpy().tolist()
myTree = ttk.Treeview(treeFrame, height=100, column=column)
myTree.place(relheight=1, relwidth=1)
myTree['show']='headings'

treescrolly = tk.Scrollbar(treeFrame, orient="vertical", command=myTree.yview)
treescrollx = tk.Scrollbar(treeFrame, orient="horizontal", command=myTree.xview)
myTree.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")

for each in column:
    myTree.column(each, width=80)
    myTree.heading(each, text=each.capitalize())

for each in data_rows:
    myTree.insert("", "end", values = each)

root.mainloop()