"""
Created on Fri Dec 29 11:24:29 2023

A simple web scrapper following an online course.
The code is based, but not copied from the examples in the
OpenClassrooms course 'Learn Python Basics'.
On this second version, we will get all the titles from
all the pages of the original UK news site, along with
the descriptions.

@author: gnmandrade
"""

# Import libraries
import csv
import requests
from bs4 import BeautifulSoup

# Define wdir
wdir = '/home/goncalo/Documents/python_projects/0-learning/testing-and-learning/OCR/'

# Define url
initial_url = "https://www.gov.uk/search/news-and-communications"


# Define functions to extract required data

def load_page_from_url(url):
    # Load page
    page = requests.get(url)

    # Parse page content
    soup = BeautifulSoup(page.content, 'html.parser')
    
    return soup


def get_titles(bs_page):
    # Find all titles
    titles_bs = bs_page.find_all('div', class_='gem-c-document-list__item-title')

    # Put titles in a list
    titles_news = [title.find('a').string for title in titles_bs]
    
    return titles_news


def get_descriptions(bs_page):
    # Extract all descriptions
    descriptions_bs = bs_page.find_all('p', class_='gem-c-document-list__item-description')
    descriptions_news = [description.string for description in descriptions_bs]
    return descriptions_news


def get_next_page_url(bs_page):
    next_page_element = bs_page.find('div', class_='govuk-pagination__next').find('a').href
    print(next_page_element)


# Test
bs_page = load_page_from_url(url)
get_next_page_url(bs_page)


# Save data to csv
headers = ['title', 'description']

# Open a file to write called data.csv
with open(wdir + 'data.csv', 'w', newline = '') as csvfile:
    # Create a writer object with the file
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(headers)
    
    # Loop all elements in titles and descriptions lists
    for i in range(len(titles_news)):
        # Create a new row with the title and description for
        # each point in the loop
        row = [titles_news[i], descriptions_news[i]]
        writer.writerow(row)