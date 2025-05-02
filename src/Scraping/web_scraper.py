import requests
from bs4 import BeautifulSoup
import pandas as pd
from rapidfuzz import fuzz
import time
import random
from urllib.parse import quote_plus

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
final_reviews = []



#Searches Goodreads given the title and author
def goodreads_search(title, author):
    #GPT:
    search_query = quote_plus(f'{title} {author}')
    gr_url = f'https://www.goodreads.com/search?q={search_query}'

    #Send a GET request to Goodreads
    #Beautiful soup will be used to parse the HTML
    result = requests.get(gr_url, headers=headers)
    soup = BeautifulSoup(result.content, 'html.parser')
    print(soup.prettify())


    #Find the title within the a hyperlink
    searched_book = soup.find("a", class_="bookTitle")
    #If no book is found with the title
    if not searched_book:
        return None

    #Searching for the tr that encloses the book title
    search_result_title = searched_book.get_text(strip=True)
    find_tr = searched_book.find_parent("tr")
    
    #Searching for the author name within the enclosed div
    search_author = find_tr.find("a", class_="authorName") if find_tr else None
    search_result_author = search_author.get_text(strip=True) if search_author else ""

    #GPT: Fuzzy matching 
    title_match_value = fuzz.token_sort_ratio(title.lower(), search_result_title.lower())
    author_match_value = fuzz.token_sort_ratio(author.lower(), search_result_author.lower())


    if title_match_value > 80 and author_match_value > 80:
        return "https://www.goodreads.com" + searched_book["href"]

    return None


def obtain_reviews(url, id, title, author, max_page = 3):
    #GPT:
    for p in range(1, max_page + 1):
        page_link = f"{url}?page={p}"

    
        #Send a GET request to Goodreads
        #Beautiful soup will be used to parse the HTML
        result = requests.get(page_link, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')
        print(soup.prettify())



    

    try: 

 



        final_reviews({

            "review_text": review_text,
            "review_rating": review_rating,
            "reviewer_id": reviewer_id,
            "upvotes": upvotes,
            "downvotes": None,
            "review_date": review_date,
            "user_shelf_tag": user_shelf_tag,
            "number_of_comments": number_of_comments
        })


    except Exception as e: 
        print("There was an error with the current page.")

    time.sleep(random.uniform(1, 2))


#Scrape Goodreads for the desired reviews about a certain book using our given
#csv file
def web_scraper(csv_file):
    #Read in the csv data:
    df = pd.read_csv('goodreads_list.csv')
    #print(df.head())

    #We want to find each book on the Goodreads website, so a url will be needed
    for _, rows in df.iterrows():
        #Pull csv ids
        book_id = rows['Book ID']
        title = str(rows['Title'])
        author = str(rows['Author'])

        #Add in a try-except block to handle exceptions. This is where we will
        #see if our url search has worked or not
        try: 
            book_url = goodreads_search(title, author)

            if book_url:
                print(f"We managed to find a {title} by the author of {author}!")
                obtain_reviews(book_url, book_id, title, author)

            else: 
                print(f"We could not find a book by the name of {title} by {author}.")

        except Exception as e:
            print(f'There was an issue with finding {title} by the author {author}.')
            continue

            #No return statement is necessary as we need to turn out results into csv format
            #in another section


#Run the program
def main():
    web_scraper("goodreads_list.csv")

    #Turn out results into a csv file:
    output_file = pd.DataFrame(final_reviews)
    output_file.to_csv("final_output.csv", index=False)
    print("Webscraping has finished!")