from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

url = "https://www.sarkariyojna.co.in/complete-list-schemes-launched-pm-narendra-modi/"
header = {'User-Agent': 'Mozilla/5.0'}

obj = open("sarkariyojna.txt","w")

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


q = Request(url,headers=header)
response = urlopen(q)

content = ''

soup = BeautifulSoup(response, "lxml")
articles = soup.find('article',id='post-154')
#for article in articles:
r2 = articles.find('div',class_='entry')


result = r2.findAll("p")


for z in result:
	rx = z.findAll('strong')


obj.write(str(result))
# obj.write(str(result))
# obj.write(str(content))
obj.close()
