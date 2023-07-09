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


site = "https://www.informationsecurity.com.tw/article/json/ajax_list.aspx?mod=1"
html = get_webpage(site)
soup = BeautifulSoup(html, "html.parser")


# 標題+連結
http = soup.find_all("a", class_="articleList_box")
for link in http:
    print(link.text)  # 標題
    print('https://www.informationsecurity.com.tw'+link['href'])  # 連結
    print("----------------------------------------------------------------")

    # 抓內文資料
    site_in = "https://www.informationsecurity.com.tw"+str(link['href'])
    html_in = get_webpage(site_in)
    soup_in = BeautifulSoup(html_in, "html.parser")
    keyword = soup_in.find_all("div", class_="tag_box w_93")
    for key in keyword:
        print(key.text)
        # 判斷關鍵字是否符合
        if ("網路釣魚" in key.text):
            print("抓到")
            ################################################################
            '''
            # 符合輸出成word
            # Initialise the Word document
            doc = docx.Document()

            doc.add_heading("Informationsecurity News", level=0)


            # 標題
            table = doc.add_table(rows=1, cols=2, style='Table Grid')
            hc = table.rows[0].cells
            hc[0].text = 'News Title'
            hc[1].text = 'Link'

            # Initialise the table
            t = doc.add_table(rows=df.shape[0], cols=df.shape[1])
            t.style = 'Table Grid'

            # Add the body of the data frame to the table
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    cell = df.iat[i, j]
                    t.cell(i, j).text = str(cell)
                
            # Save the Word doc
            doc.save('result.docx')
            '''
            ################################################
        else:
            print("不符")


########################################################################
# 標題
titles = soup.find_all("div", class_="title")  # find_all要用迴圈下去跑，不然會報錯
for title in titles:
    print(title.text)


# 一個一個印出要的資料
for articleList_box in http:
    print(articleList_box.a.string)  # 取得文章標題
    print("https://www.informationsecurity.com.tw" +
          articleList_box.a.get("href"))  # 取得文章連結


#data = soup.find_all("div", id="_container")[0].text

#num = re.findall(r"\d+", data.text)
#num = np.array(num)
# print(num[1])
