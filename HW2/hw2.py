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
# 嘗試抓特定區塊資料


site = "https://www.informationsecurity.com.tw/article/article_list.aspx?mod=1"
html = get_webpage(site)
soup = BeautifulSoup(html, "html.parser")

data = soup.find_all("div", id="_container")[0].text

print(data)

#num = re.findall(r"\d+", data.text)
#num = np.array(num)
# print(num[1])

########################################################################
'''

df = pd.DataFrame()
site = "https://www.informationsecurity.com.tw/article/article_list.aspx?mod=1"
html = get_webpage(site)
df = pd.read_html(html)[0]
'''

'''
soup = BeautifulSoup(html, "html.parser")
artitle = soup.find("a", class_="articleList_box")
print(artitle)
#print(soup)
'''
#df = pd.concat([df, pd.read_html(html)[0]])
