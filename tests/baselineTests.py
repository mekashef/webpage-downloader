import os, sys, re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def testIceCream():
    # specify the url
    quote_page ="https://www.nytimes.com/interactive/2014/07/01/dining/the-master-ice-cream-recipe.html?mtrref=undefined&gwh=CDD5B181CD807718833B461E468D1E5B&gwt=pay&assetType=PAYWALL"

    # query the website and return the html to the variable ‘page’
    page = urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")

    print(soup)


testIceCream()