import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import docx
from docx import Document
from docx.text.paragraph import Paragraph
from docx.shared import Inches
import re
import requests,random
import time
from datetime import datetime

user_agents = ['User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
def get_html(url):
   headers = {'User-Agent':random.choice(user_agents)}
   resp = requests.get(url,headers = headers)
   return resp.text

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
#定義line Notify

def LineNotify(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {
        "message": msg
    }
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)


############################ 嘗試抓文章特定區塊資料 ############################

site = "https://www.informationsecurity.com.tw/article/json/ajax_list.aspx?mod=1"
html = get_webpage(site)
soup = BeautifulSoup(html, "html.parser")

# 標題+連結
#http = soup.find_all("a", class_="articleList_box")
http2 = soup.find("a", class_="articleList_box")
#抓最新的那則新聞，目的是取出當中的最大index
news_link_0 = 'https://www.informationsecurity.com.tw'+http2['href'] 

#讀取索引終點
MaxIndex = re.findall(r"\d+", news_link_0)[0] #最大索引值
MaxIndex = int(MaxIndex)
#讀取索引起點
f = open('initial.txt')
Initial_Index=f.read()
Initial_Index=int(Initial_Index)

#抓年份日期
date = time.ctime()
date = date.split()
#print(date[4])
year = date[4]
#讀取關鍵字
f = open('list.txt')
f=f.read()
#print(f)
#更新關鍵字年份
obj = re.sub(str(int(year)-1),str(year),f)
#print(obj)
with open("list.txt","w") as file:
    file.write(obj)

#讀取關鍵字
f = open('list.txt')
#關鍵字輸出成list
text = []
for line in f.readlines():
    text.append(line)
f.close
list = []
#消除\n
for sub in text:
    list.append(sub.replace("\n", ""))
print(list)

#################################### 開始搜索 ####################################
output="" 
for i in range(0,MaxIndex-Initial_Index):

    #title = http.text
    news_link = 'https://www.informationsecurity.com.tw/article/article_detail.aspx?aid='+str(MaxIndex-i)+'&mod=1'

    # 抓內文資料
    site_in = news_link
    html_in = get_webpage(site_in)
    soup_in = BeautifulSoup(html_in, "html.parser")
    #title = soup_in.find("h1", class_="title_content w_93").text
    #print(title)

    #抓關鍵字
    keyword = soup_in.find_all("div", class_="tag_box w_93")
    for key in keyword:
        for i in range(len(list)):
            # 判斷關鍵字是否符合
            if (list[i] in key.text):
                #符合即輸出
                title = soup_in.find("h1", class_="title_content w_93").text
                news=title+"\n"+news_link+"\n\n"
                print(news) 
                #print(output)
                output=output+news
                break

 
if __name__ == "__main__" and output != '' :
    token = "fpz5bCQsWqNjyyZVe7OeLP0tFcGT25gzUU41Y5HyHmy" #從LINE Notify取得的權杖(token)   
    msg = "最新相關文章：\n" + output #要在LINE上跳出的提示訊息

    LineNotify(token, msg)

################################################

#更新起點

Initial_Index=MaxIndex 

with open("initial.txt","w") as file:
    file.write(str(Initial_Index))
            
################################################
"""
 *              ,----------------,              ,---------,
 *         ,-----------------------,          ,"        ,"|
 *       ,"                      ,"|        ,"        ,"  |
 *      +-----------------------+  |      ,"        ,"    |
 *      |  .-----------------.  |  |     +---------+      |
 *      |  |                 |  |  |     | -==----'|      |
 *      |  |  I LOVE STI!    |  |  |     |         |      |
 *      |  |  No Bug Plz     |  |  |/----|`---=    |      |
 *      |  |  C:\>_Yoora     |  |  |   ,/|==== ooo |      ;
 *      |  |                 |  |  |  // |(((( [33]|    ,"
 *      |  `-----------------'  |," .;'| |((((     |  ,"
 *      +-----------------------+  ;;  | |         |,"
 *         /_)______________(_/  //'   | +---------+
 *    ___________________________/___  `,
 *   /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 *  / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
 * /_==__==========__==_ooo__ooo=_/'   /___________,"
 *
 *
 *
 *
 *      ┌─┐       ┌─┐                           
 *   ┌──┘ ┴───────┘ ┴──┐                           
 *   │                 │                           
 *   │       ───       │                           
 *   │   >        <    │                           
 *   │                 │                           
 *   │   ...  ⌒  ...   │                                                    
 *   │                 │
 *   └───┐         ┌───┘
 *       │         │
 *       │         │
 *       │         │
 *       │         └──────────────┐
 *       │                        │
 *       │                        ├─┐
 *       │                        ┌─┘
 *       │                        │
 *       └─┐  ┐  ┌───────┬──┐  ┌──┘
 *         │ ─┤ ─┤       │ ─┤ ─┤
 *         └──┴──┘       └──┴──┘
 *               不要電我><
 *               
 *
 *
 *
 *
 *      ┌─┐       ┌─┐ + +
 *   ┌──┘ ┴───────┘ ┴──┐++
 *   │                 │
 *   │       ───       │++ + + +
 *   ███████───███████ │+
 *   │                 │+
 *   │       ─┴─       │
 *   │                 │
 *   └───┐         ┌───┘
 *       │         │
 *       │         │   + +
 *       │         │
 *       │         └──────────────┐
 *       │                        │
 *       │                        ├─┐
 *       │                        ┌─┘
 *       │                        │
 *       └─┐  ┐  ┌───────┬──┐  ┌──┘  + + + +
 *         │ ─┤ ─┤       │ ─┤ ─┤
 *         └──┴──┘       └──┴──┘  + + + +
 *           我要成為厲害的資安人
 *              
 *

 """