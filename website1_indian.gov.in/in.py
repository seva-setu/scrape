import requests
from lxml import html
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#csvWriter = csv.writer(open("yojna.csv", 'w'), delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)


link=list()
title=list()
website=list()
for i in range(1,100):
	url = "https://india.gov.in/my-government/schemes?jurisdiction=All&ministry=All&field_st_dept_tid=All&title=&page="+str(i)

	link.append(url)

url1="https://india.gov.in/my-government/schemes"
session=requests.Session()

def get_yojna(url):
	page=session.get(url)
	return page.text

def parse(url):
	source=get_yojna(url)
	tree=html.fromstring(source)
	return tree

tree = parse(url1)
name=tree.xpath('//div[contains(@class, "view-metadata-for-schemes")]//div[@class="item-list"]//a//text()')
web=tree.xpath('//div[contains(@class, "view-metadata-for-schemes")]//div[@class="item-list"]//a//@href')
for i in range(len(name)):
	title.append(name[i])
for i in range(len(web)):
	website.append(web[i])
for l in link:

	tree=parse(l)
	name=tree.xpath('//div[contains(@class, "view-metadata-for-schemes")]//div[@class="item-list"]//a//text()')
	web=tree.xpath('//div[contains(@class, "view-metadata-for-schemes")]//div[@class="item-list"]//a//@href')

	for i in range(len(name)):
		title.append(name[i])
	for i in range(len(web)):
		website.append(web[i])


scheme_info=[dict() for r in xrange(len(title))]

i=0
for dic in scheme_info:
	dic['scheme_name'] = title[i]
	dic['url'] = website[i]
	i=i+1
import pprint
pprint.pprint(scheme_info)
field_names=["scheme_name", "url"]
with open("indian_gov.csv", "w") as f:
	writer= csv.DictWriter(f,field_names)
	for obj in scheme_info:
		writer.writerow(obj)

