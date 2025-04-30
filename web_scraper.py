import requests
from bs4 import BeautifulSoup
import pandas as pd

#Read in the csv data:
df = pd.read_csv('goodreads_list.csv')
print(df.head())

#We want to find each book on the Goodreads website, so a url will be needed
for i in df:



#Now let's begin searching the Goodreads website using GET requests
#Beautiful soup will then be used to parse the HTML
goodreads_request_test = requests.get("https://www.goodreads.com/")
