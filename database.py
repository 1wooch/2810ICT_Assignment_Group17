# # import required libraries and packages
# import csv
# import sqlite3 as sql
# import pandas as pd
#
# # set max row display
# pd.options.display.max_rows = 2
#
# # must have dataset saved in C drive to use
# dataset = pd.read_csv(r'C:\penalty_data_set.csv')

# print(dataset)


import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd

root = tk.Tk()
root.geometry("500x500")
root.pack_propagate(False)
root.resizable(0, 0)

frame1 = tk.LabelFrame(root, text="CSV Data")
frame1.place(height=250, width=500)

file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=400, rely=0.65, relx=0)

button1 = tk.Button(file_frame, text="Browse A File", command=lambda: file_dialog())
button1.place(rely=0.65, relx=0.5)

button2 = tk.Button(file_frame, text="Load File", command=lambda: load_csv_data())
button2.place(rely=0.65, relx=0.3)

label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0, relx=0)

tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")

def file_dialog():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("csv files", "*.csv"),("All Files", "*.*")))
    label_file["text"] = filename
    return None

def load_csv_data():
    file_path = label_file["text"]
    try:
        csv_filename = r"{}".format(file_path)
        df = pd.read_csv(csv_filename)
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have entered is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)

    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)
    return None

def clear_data():
    tv1.delete(*tv1.get_children())



root.mainloop()