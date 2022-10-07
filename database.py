import tkinter
import tkinter.font as tkFont
from tkinter import TclError, ttk
import pandas as pd

data_header = ['Financial Year', 'Month', 'Offence Code', 'Offence Description', 'Legislation', 'Section Clause',
          'Penalty Amount', 'Camera Offence', 'Camera Type', 'Camera Location', 'Camera Location Details', 'School Zone',
          'Speed Range', 'Speed Offence', 'Point to Point Offence', 'Red Light Camera Offence', 'Speed Camera Offence',
          'Seatbelt Offence', 'Mobile Phone Offence', 'Parking Offence', 'Criminal Infringement Notice Scheme Offence',
          'Food Safety Offence', 'Non-Motor Vehicle Offence', 'Number of Penalty Notices',
          'Total Value of Penalty Notices']
data = pd.read_csv("penalty_data_set_2.csv")
data_rows = data.to_numpy().tolist()

class App(tkinter.Tk):

    _detached = set()

    def tree_reset(self):
        children = list(self._detached) + list(self.tree.get_children())
        self._detached = set()
        self.filter_re.set('')
        for ix, item_id in enumerate(children):
            self.tree.reattach(item_id, '', ix)

    def tree_filter(self, *args):
        children = list(self._detached) + list(self.tree.get_children())
        self._detached = set()
        query = self.filter_re.get()
        i_r = -1
        for _, item_id in enumerate(children):
            text = ' '.join(self.tree.item(item_id, 'values'))
            if query in text:
                i_r += 1
                self.tree.reattach(item_id, '', i_r)
            else:
                self._detached.add(item_id)
                self.tree.detach(item_id)


    def __init__(self):
        super().__init__()
        self.title('NSW Traffic Penalty Offences')
        self.geometry('200x200')
        self.resizable(True, True)
        self.minsize(200, 200)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.filter_re = tkinter.StringVar()
        ttk.Label(self, text = 'Filter: ').grid(column = 0, row = 0, sticky = tkinter.W)
        searchfield = ttk.Entry(self, textvariable = self.filter_re).grid(
            column = 1, row = 0, sticky='nsew')
        ttk.Button(self, text = 'Reset', command = self.tree_reset).grid(
            column = 2, row = 0, columnspan=2, sticky = tkinter.E)
        self.filter_re.trace("w", self.tree_filter)

        self.tree = ttk.Treeview(self, column = data_header, height=30)
        scroll_x = ttk.Scrollbar(self, command = self.tree.xview, orient = tkinter.HORIZONTAL)
        scroll_x.grid(column = 0, row = 2, columnspan = 3, sticky = 'we')
        scroll_y = ttk.Scrollbar(self, command = self.tree.yview, orient = tkinter.VERTICAL)
        scroll_y.grid(column = 3, row = 1, sticky='ns')
        self.tree.configure(xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        self.tree.column('#0', width = 1)

        for label in self.tree["column"]:
            self.tree.heading(label, text = label,
            command = lambda column = label: tree_sortby(self.tree, column))
            self.tree.column(label, width = tkFont.Font().measure(label.title()))

        for row in data_rows:
            self.tree.insert('', 'end', values = row)

        self.tree.grid(column=0, row=1, columnspan=3, sticky='nsew')


if __name__ == "__main__":
    app = App()
    app.mainloop()