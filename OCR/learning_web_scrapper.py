#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:24:29 2023

A simple web scrapper following an online course.
The code is based, but not copied from the examples in the
OpenClassrooms course 'Learn Python Basics'.

@author: gnmandrade
"""

# Import libraries
import csv
import requests
from bs4 import BeautifulSoup

# Define wdir
wdir = '/home/goncalo/Documents/python_projects/0-learning/testing-and-learning/OCR/'

# Define url
url = "https://www.gov.uk/search/news-and-communications"
#url = "https://www.google.com"
# Load page
page = requests.get(url)

# Print source html
#print(page.content)

# Parse page content
soup = BeautifulSoup(page.content, 'html.parser')

########
# Check different elements
########

# Get HTML page title
print(soup.title)
# Get HTML page title as a string
print(soup.title.string)

# Find all elements with the <a> tag
# This works similarly to a list, but is actually a 
# bs4.element.ResultSet
a_tags = soup.find_all('a')
#print(a_tags)

# Find element with the id = 'js-results'
link1_id = soup.find(id="js-results")
#print(link1_id)


# Find all p elements with class "govuk-body"
p_class_govuk_body = soup.find_all("p", class_="govuk-body")
#print(p_class_govuk_body)


# Find all titles
titles_bs = soup.find_all('div', class_='gem-c-document-list__item-title')

# Put titles in a list
titles_news = [title.find('a').string for title in titles_bs]
#print(titles_news)

# Print the titles
#for x in titles_news:
#    print(x)
#    print()

# Extract all descriptions
descriptions_bs = soup.find_all('p', class_='gem-c-document-list__item-description')
descriptions_news = [description.string for description in descriptions_bs]

# Print the descriptions
#for x in descriptions_news:
#    print(x)
#    print()

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