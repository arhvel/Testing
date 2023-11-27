# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:13:06 2023

@author: VictorAdeyemo
"""

import requests
from bs4 import BeautifulSoup
urlFilm = "https://quotes.toscrape.com/author/Marilyn-Monroe/"
page = requests.get(urlFilm)
soup = BeautifulSoup(page.content, "html.parser")
soup


name = soup.find("h3", class_="author-title")
name.text

spanBorn = soup.find("span", class_="author-born-date")
print(spanBorn.text)

bornLocation = soup.find("span", class_ ="author-born-location")
bornLocation.text

description = soup.find("div", class_ = "author-description")
description.text


urlFilm = "https://quotes.toscrape.com/author/Jane-Austen/"
page = requests.get(urlFilm)
soup = BeautifulSoup(page.content, "html.parser")
soup


name = soup.find("h3", class_="author-title")
print(name.text)

spanBorn = soup.find("span", class_="author-born-date")
print(spanBorn.text)

bornLocation = soup.find("span", class_ ="author-born-location")
bornLocation.text

description = soup.find("div", class_ = "author-description")
description.text



## Data Munging

### date formatting
from datetime import datetime

dateFormat = '%B %d %Y'

u = list(spanBorn.text)
u.remove(",")
date = ''.join(e for e in u)
date

dateObject = datetime.strptime(spanBorn.text,dateFormat)


### Location formatting

bornLocation.text

twc = bornLocation.text.replace('in',"").split(",")
Country = twc[2]
City = twc[1]
Town = twc[0]


## Data Analysis
import requests
import datetime
from bs4 import BeautifulSoup


# Storing the URLs for different authors
urls = []
urls.append("https://quotes.toscrape.com/author/J-K-Rowling/")
urls.append("http://quotes.toscrape.com/author/Jane-Austen/")
urls.append("https://quotes.toscrape.com/author/Albert-Einstein/")
urls.append("http://quotes.toscrape.com/author/Marilyn-Monroe/")
urls.append("http://quotes.toscrape.com/author/Andre-Gide/")
urls.append("http://quotes.toscrape.com/author/Thomas-A-Edison/")
urls.append("http://quotes.toscrape.com/author/Eleanor-Roosevelt/")
urls.append("http://quotes.toscrape.com/author/Steve-Martin/")
urls.append("http://quotes.toscrape.com/author/Bob-Marley/")
urls.append("http://quotes.toscrape.com/author/Dr-Seuss/")
urls.append("http://quotes.toscrape.com/author/Douglas-Adams/")
urls.append("http://quotes.toscrape.com/author/Friedrich-Nietzsche/")
urls.append("http://quotes.toscrape.com/author/Mark-Twain/")
urls.append("http://quotes.toscrape.com/author/Pablo-Neruda/")
urls.append("http://quotes.toscrape.com/author/Ralph-Waldo-Emerson/")
urls.append("http://quotes.toscrape.com/author/Mother-Teresa/")
urls.append("http://quotes.toscrape.com/author/Garrison-Keillor/")
urls.append("http://quotes.toscrape.com/author/Charles-M-Schulz/")
urls.append("http://quotes.toscrape.com/author/William-Nicholson/")


# Looping through all the pages
authors = []
for url in urls:

    # Get the page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Get the information
    spanBorn = soup.find("span", class_="author-born-date")
    spanLocation = soup.find("span", class_="author-born-location")
    divDescription = soup.find("div", class_="author-description")
    h3AuthorTitle = soup.find("h3", class_="author-title")  
    if (h3AuthorTitle.text.find("\n")!=-1):
        strAuthorTitle = h3AuthorTitle.text[:h3AuthorTitle.text.find("\n")] # Just take the first line
    else:
        strAuthorTitle = h3AuthorTitle.text
        
    # Munging for born date
    strBornDate = spanBorn.text
    dateTimeObject = datetime.datetime.strptime(strBornDate, '%B %d, %Y')

    # Munging for born place
    strBornLocation = spanLocation.text
    strBornLocation = strBornLocation.replace("in ", "")
    iLastComma = strBornLocation.rfind(",")
    if (iLastComma == -1):
        strCountry = strBornLocation
        strTownState = ""
    else:
        strCountry = strBornLocation[iLastComma+2:]
        strTownState = strBornLocation[:iLastComma]
    iSecondComma = strTownState.rfind(",") # Checking if there is a second comma
    if (iSecondComma == -1):
        strState = strTownState
        strTown = ""
    else:
        strState = strTownState[iSecondComma+2:]
        strTown = strTownState[:iSecondComma]

    # Storing into a list
    author = [strAuthorTitle, dateTimeObject.date().year, dateTimeObject.date().month, dateTimeObject.date().day, strCountry, strState, strTown]
    authors.append(author)

    # Printing the stored item out
    print(author)

