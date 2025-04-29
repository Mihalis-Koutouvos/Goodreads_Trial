import requests

#Testing the Goodreads page:
goodreads_request_test = requests.get("https://www.goodreads.com/")

#Checking the status code:
print(goodreads_request_test)
print(goodreads_request_test.content)