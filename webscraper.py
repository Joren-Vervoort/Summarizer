# -*- coding: utf-8 -*-
"""Webscraper

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PMJNK3CipLby_AKx2OofmJv2FF46IkMr

## **Connecting your google drive**
"""

from google.colab import drive
drive.mount('/content/gdrive')

"""## **Libraries**"""

from bs4 import BeautifulSoup
import requests

"""## **Webscraper**"""

def book_finder():

  book_search = input("Book title: ")
  book_search = book_search.replace(" ","+")

  search_link = f"https://www.gutenberg.org/ebooks/search/?query={book_search}&submit_search=Go%21"

  search_request = requests.get(search_link)
  print(search_link, search_request.status_code)
  soup = BeautifulSoup(search_request.text,'html') #lxml

  link_list=[]

  for tag in soup.find_all('li', {"booklink"}):
      for anchor in tag.find_all('a'):
          link_list.append(anchor['href'])

  book_number = link_list[0].lstrip("/ebooks/")

  book_link = f"https://www.gutenberg.org/files/{book_number}/{book_number}-h/{book_number}-h.htm"
  print(book_link)
  ##################################

  book_request = requests.get(book_link)
  print(search_link, book_request.status_code)
  soup = BeautifulSoup(book_request.text,'html') #lxml

  text=[]

  for tag in soup.find_all('body'):
      for anchor in tag.find_all('p'):
          text.append(anchor)

  return text, soup

#Executing the function

text, soup = book_finder()

#Example of paragraphs 3 and 4

print(text[3:5])