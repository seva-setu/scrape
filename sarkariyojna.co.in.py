from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import csv	
import pandas as pd
from lxml import etree

url = "https://www.sarkariyojna.co.in/complete-list-schemes-launched-pm-narendra-modi/"
header = {'User-Agent': 'Mozilla/5.0'}

obj = open("temp.html","w")

data = {
	'_title' : [],
    'link' : [],
    'detail' : [],
    'ministry' : [],
    'sector' : []
}

header = {
	"Host" : "www.sarkariyojna.co.in",
	"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language" : "en-US,en;q=0.5",
	"Connection" : "close"
}

#post-154 > div.entry > p:nth-child(8)

q = Request(url,headers=header)
response = urlopen(q)
#htmlparser = etree.HTMLParser()

soup = BeautifulSoup(response, "lxml")
content = soup.select("#post-154 .entry > p:nth-of-type(8)")
content2 = soup.select("#post-154 .entry > p:nth-of-type(7) + strong:nth-of-type(3)")


#content2 = content.find("div",{"class":"entry"})
print(content2)
obj.write(str(content))
obj.close()


# /html/body/div[4]/div[1]/main/section/article/div[3]/h3[3]
# /html/body/div[4]/div[1]/main/section/article/div[3]/p[16]