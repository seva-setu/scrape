# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:49:02 2017

@author: satejwagle
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas import DataFrame
import requests
from lxml import html
import cookielib

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

        
find_between( str(rj.content), "theme_token\":\"", "\"" )

df = DataFrame(columns=('source','index','title', 'gov_link','details'))
l = 0
header = {
"Host": india.gov.in
"Connection: keep-alive
"Content-Length": 8273
"Accept": application/json, text/javascript, */*; q=0.01
"Origin": https://india.gov.in
"X-Requested-With": XMLHttpRequest
"User-Agent": Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
"Content-Type": application/x-www-form-urlencoded; charset=UTF-8
"Referer": https://india.gov.in/my-government/schemes
"Accept-Encoding": gzip, deflate, br
"Accept-Language": en-US,en;q=0.8
"Cookie": has_js=1; _ga=GA1.3.856886001.1491668108; _gat=1
}

form_data = 
for i in range(0,10):
search_str = ""
section_url = "https://india.gov.in/my-government/schemes"
f_url = section_url+search_str
html = urlopen(f_url).read()
soup = BeautifulSoup(html, "lxml")
content = soup.find("div",{"id": "content"})
content_2 = content.find("div",{"class": "region region-three-25-50-25-second"})
results = content_2.findAll("div",{"class" : "views-field views-field-title"})
    for j in range(0,len(results)):
       link = results[j].a["href"]
       name = str(results[j].a.string)
       page = section_url+link
       html_page = urlopen(page).read()
       p = BeautifulSoup(html_page,"lxml")
       gov_link = p.find("ol",{"class":"result-page main_data"}).a['href']
       detail = p.find("ol",{"class":"result-page main_data"}).p.string
       df.loc[l] = [f_url,str(l+1),name,gov_link,detail]
       l= l+1
            
df.to_csv('/Users/satejwagle/Seva Setu/sample.csv')
results[1]

session = requests.session()
rj = session.get("https://india.gov.in/my-government/schemes")
token = find_between( str(rj.content), "theme_token\":\"", "\"" )

50a1555819ee6ac393015ac41fe81d26
50a1555819ee6ac393015ac41fe81d26
50a1555819ee6ac393015ac41fe81d26

1D9riGRljR2-N-CV0Z_8JpxmwtcDGsvwn1JJeDBPSX8