import feedparser
import csv
import json
#import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

def extract(query):
    url= "http://rss.jobsearch.monster.com/rssquery.ashx?q="
    query= "engineer"
    final_url = url + query

    url_xml = urlopen(final_url)
    xml = url_xml.read()
    print(xml)
    url_xml.close()
    soup_page = BeautifulSoup(xml,features="lxml")
    list = soup_page.findAll("item")

    create(list)

def create(list):
    for item in list:
        print("\n")
        print(item.title.text)
        print(item.link.text)
        print(item.description.text)
        print(item.pubDate.text)
        print("\n")
 
    

query="engineer"
extract(query)