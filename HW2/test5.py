import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import docx
from docx import Document
from docx.shared import Inches
import re


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2,
         'permissions.default.stylesheet': 2}
chrome_options.add_experimental_option("prefs", prefs)

#

url = "https://www.informationsecurity.com.tw/article/article_list.aspx?mod=1"
driver = webdriver.Chrome()
driver.get(url)

#

####
roll = 1000
while True:
    h_before = driver.execute_script(
        'return document.documentElement.scrollTop')
    time.sleep(0.3)
    driver.execute_script(f'window.scrollTo(0,{roll})')
    time.sleep(0.3)
    h_after = driver.execute_script(
        'return document.documentElement.scrollTop')
    roll += 500
    print(h_after, h_before)
    if h_before == h_after:
        break

content = driver.page_source
data = pd.read_html(content)
table = pd.DataFrame(data[0])
print(table)


http = soup.find_all("a", class_="articleList_box")
for link in http:
    title = link.text
    news_link = 'https://www.informationsecurity.com.tw'+link['href']
