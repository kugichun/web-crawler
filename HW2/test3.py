import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import docx
from docx import Document
from docx.shared import Inches
import re

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
# 抓內文資料
site_in = "https://www.informationsecurity.com.tw/article/article_detail.aspx?aid=10551&mod=1"
html_in = get_webpage(site_in)
soup_in = BeautifulSoup(html_in, "html.parser")
keyword = soup_in.find_all("div", class_="tag_box w_93")


for key in keyword:
    print("型態：", type(key.text))
    print(key.text)

    if ("網路釣魚" in key.text):
        print("抓到")
        # 輸出成word

    else:
        print("不符")

    #a = list(key.text)
    # print(a)
    # keywords.append(key)
    # print(keywords.text)
