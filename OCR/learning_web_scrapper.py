#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:24:29 2023

A simple web scrapper following an online course.

@author: gnmandrade
"""

# Import libraries
import requests
from bs4 import BeautifulSoup

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


