# import required libraries and packages
import sqlite3 as sql
import pandas as pd

# establish connection with traffic dataset
con = sql.connect("memory")
wb = pd.read_excel('penalty_data_set_2', sheet_name = None)
cur = con.cursor

# create tables
for table, df in dfs.items():
    df.to_sql(table, db)

# commit and close
con.commit()
con.close()