import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import docx
from docx import Document
from docx.shared import Inches
import re
from selenium import webdriver


#########################################################################
# 定義函式，以取得html_page文本


def get_webpage(url):
    html_page = requests.get(url)

    if html_page.status_code != 200:
        print("invalid url", html_page.status_code)
        return None
    else:
        return html_page.text

#########################################################################


driver = webdriver.Chrome()
driver.get("https://www.informationsecurity.com.tw/article/article_list.aspx?mod=1")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

site = "https://www.informationsecurity.com.tw/article/json/ajax_list.aspx?mod=1"
html = get_webpage(site)
soup = BeautifulSoup(html, "html.parser")
