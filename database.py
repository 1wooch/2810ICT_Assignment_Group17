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


import sys
import os
import time
import sqlite3
import re
import wx
import wx.lib.mixins.inspection
import wx.lib.mixins.listctrl as listmix

AppTitle = "NSW Traffic Penaly Data"

class MyConnection(object):
    def __init__(self):
        self.database_dir = wx.GetApp().GetDatabaseDir()
        dbFile = os.path.join(self.database_dir, "penalty_data_set_2.csv")