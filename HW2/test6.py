import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import docx
from docx import Document
from docx.shared import Inches
import re

b = ""
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
# 嘗試抓特定區塊資料


site = "https://www.informationsecurity.com.tw/article/article_list.aspx?mod=1"
html = get_webpage(site)
soup = BeautifulSoup(html, "html.parser")


# 標題+連結
http = soup.find_all("a", class_="articleList_box")
for link in http:
    title = link.text
    news_link = 'https://www.informationsecurity.com.tw'+link['href']
    print(news_link)
