import requests
import csv
import json
import pandas as pd

def filter():
    col_list = ["title","link","description","date"]
    
   
    URL=""
    df = pd.read_csv(URL,usecols=col_list)

   #d=df_filtered.filter(col1) #filter by columns
   #d=d.rename(columns={"title": "job title"}) #renaming columns
    df=df.set_index("title") #changing keys
    df.to_json (r'jobs.json')
   
filter()