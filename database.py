# import required libraries and packages
import csv
import sqlite3 as sql
import pandas as pd

# set max row display
pd.options.display.max_rows = 2

# must have dataset saved in C drive to use
dataset = pd.read_csv(r'C:\penalty_data_set.csv')

print(dataset)


