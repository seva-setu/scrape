from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree

url = "https://www.sarkariyojna.co.in/complete-list-schemes-launched-pm-narendra-modi/"
header = {'User-Agent': 'Mozilla/5.0'}

obj = open("sarkariyojna.csv","w")

data = {
	'title' : [],
    'link' : [],
    'detail' : [],
    # 'ministry' : [],
    # 'sector' : []
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
entry_list = articles.find('div',class_='entry')


##for fetching the title
title_list = []
for element in entry_list.select('h3'):
	soup = BeautifulSoup(element.get_text(),"lxml")
	title_list.append(soup.find('p').get_text())

title_list = title_list[0:-61]
# print(len(title_result))

result = []
for element in entry_list.select('p'):
	if element.strong != None:
		result.append(element)

result = result[1:]

## for the detail list
detail_list = []
# print(len(result))
for x in range(0,len(result),2):
	sentence = str(result[x])
	index = sentence.rfind("</strong>") + 10
	detail_list.append(sentence[index:-4].strip())

# print(len(detail_list))

##for the website link
link_list = []
for x in range(1,len(result),2):
	sentence = str(result[x])
	index = sentence.rfind("</strong>") + 10
	link_list.append(sentence[index:-4].strip())

# print(len(link_list))

data['title'] = title_list
data['detail'] = detail_list
data['link'] = link_list

print(len(data['title']))
print(len(data['detail']))
print(len(data['link']))

dogData = pd.DataFrame( data )
dogData.to_csv("sarkariyojna.csv")
