import requests
from bs4 import BeautifulSoup
import pandas as pd
from rapidfuzz import fuzz
import time
import random

#Read in the csv data:
df = pd.read_csv('goodreads_list.csv')
print(df.head())

#GPT used here: I wanted to avoid errors with incoming GET requests and needed a way 
#to get around it. GPT recommended using an agent to make it seem like my code is coming 
#from a valid browser.
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Macintoch; Apple Silicon Mac OS X 14_0) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/123.0.0.0 Safari/537.36'
    )
}

#Define other variables here:
#List of dictionaries
reviews = []


#Scraper csv files
def web_scraper(csv_file):


    return 


def goodreads_search(title, author):
    book = 

    gr_url = f'https://www.goodreads.com/search?q={book}'



    #Beautiful soup will be used to parse the HTML
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content, 'html.parser')

    return 



def obtain_reviews(url, id, title, author):


    return 

#We want to find each book on the Goodreads website, so a url will be needed
for i, rows in df.iterrows():



    #Add in a try-except block to handle exceptions
    try: 


    except Exception as e:
        print(f'We could not find a book by the name of {title} by {author}.')
        continue



#Turn out results into a csv file:
output_file = pd.DataFrame(reviews)
output_file.to_csv("final_output.csv", index=False)

    

#Now let's begin searching the Goodreads website using GET requests
#Beautiful soup will then be used to parse the HTML




