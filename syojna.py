import requests
from lxml import html
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
csvWriter = csv.writer(open("yojna.csv", 'w'), delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

title1=list()
link1=list()
detail1=list()
url="https://www.sarkariyojna.co.in/complete-list-schemes-launched-pm-narendra-modi/"
session=requests.Session()


def get_yojna(url):
	page=session.get(url)
	return page.text

def parse(url):
	source=get_yojna(url)
	tree=html.fromstring(source)
	return tree

tree=parse(url)
name=tree.xpath('//div[@class="entry"]//h3/text()')
p_tags=tree.xpath('//div[@class="entry"]//p')
p_tags=p_tags[2:268]
name=name[:49]
for n in name:
	title1.append(n)
for p in p_tags:
	strong_tags = p.xpath('.//strong')
	text=p.xpath('.//text()')

	if len(strong_tags) == 1:
		link1.append(text[1])

	elif len(strong_tags) == 2:
		detail1.append(text[-1])
scheme_info=[dict() for r in xrange(len(title1))]

i=0
for dic in scheme_info:
	dic['title'] = title1[i]
	dic['link'] = link1[i]
	dic['detail'] = detail1[i]
	i=i+1

field_names=["title", "link", "detail"]
with open("yojna.csv", "w") as f:
	writer= csv.DictWriter(f,field_names)
	for obj in scheme_info:
		writer.writerow(obj)


