import requests
from bs4 import *
from selenium import webdriver
import pandas as pd
import argparse
import re
import os
from selenium.webdriver.support import ui
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Create the Chrome driver with the configured options.
chrome_options = Options()
chrome_options.add_argument("--headless")  # Dont show how it works in GUI
driver = webdriver.Chrome(options=chrome_options)


# Prepare the URL for search
item_category= 'men outfits streetwear'
url = 'https://in.pinterest.com/search/pins/?q=' + \
    item_category.replace(" ", "%20")

# wait and get the query page
driver.implicitly_wait(15)
driver.get(url)
driver.implicitly_wait(15)

all_pin_data = []

while 1:
    # scroll
    driver.execute_script("window.scrollBy(0,10000)")
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,10000)")
    time.sleep(3)

    # get the html 
    page_source = driver.page_source
    page = BeautifulSoup(page_source, 'html.parser')

    # Here we take divs which have a with href as pin number
    images = page.find_all('div', "Yl- MIw Hb7")

    all_pin_data.extend(images)
    all_pin_data = list(set(all_pin_data))
    if len(all_pin_data) > 10:
        break


# get links for individual pages of all the Pins
hrefs = []
for i in range(len(all_pin_data)):
    hrefs.append(all_pin_data[i].find('img')['src'])

for url in hrefs:
    print(url)
    urltoshow=url

