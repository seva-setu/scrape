from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree
import time
from indiagov_scheme_url_list import url_list

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
                            'Upgrade-Insecure-Requests': '1',
                            'x-runtime': '148ms'}
#
# obj = open("sarkariyojna.csv","w")
# url_list = []
#
# #For fetching the Urls
# for i in range(1,5):
# 	url = "https://india.gov.in/my-government/schemes?jurisdiction=All&ministry=All&field_st_dept_tid=All&title=&page=" + str(i)
# 	q = Request(url,headers=header)
# 	response = urlopen(q)
# 	if response.status == 200:
# 		soup = BeautifulSoup(response, "lxml")
# 		data = soup.select('#block-system-main > div > div.region.region-three-25-50-25-second > div > div.panel-pane.pane-views.pane-metadata-for-schemes.no-title.block > div > div > div > div.view-content > div > ul')
# 		data = data[0]
# 		links = data.findAll('a')
# 		for link in links:
# 			url = 'https://india.gov.in' + link['href']
# 			url_list.append(url)
# 	else:
# 		break

data = {
	'title' : [],
    'link' : [],
    'detail' : [],
    'ministry' : [],
    'sector' : []
}


for url in url_list:
	data['ministry'].append('')
	data['sector'].append('')
	q = Request(url,headers=header)
	response = urlopen(q)

	#For fetching the details
	soup = BeautifulSoup(response, "lxml")
	paragraph = soup.select('#block-system-main > div > div > div > div.panel-pane.pane-views.pane-metadata.no-title.block > div > div > div > div > ol > li > div.views-field.views-field-body > div > p')
	paragraph = paragraph[0]
	detail = paragraph.get_text()
	data['detail'].append(detail)


	#For fetching the links
	head_link = soup.select('#block-system-main > div > div > div > div.panel-pane.pane-views.pane-metadata.no-title.block > div > div > div > div > ol > li > h3 > a')
	head_link = head_link[0]
	data['title'].append(head_link.get_text())
	link = head_link['href']
	data['link'].append(link)

dogData = pd.DataFrame( data )
dogData.to_csv("indian.gov.in.csv")
