from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
from lxml import etree



# header = {
# 	"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
# 	"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# 	"Accept-Language" : "en-US,en;q=0.5",
# 	"Connection" : "close"
# }

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
                            'Upgrade-Insecure-Requests': '1',
                            'x-runtime': '148ms'}

fo = open("indiagov_scheme_url_list.py", "a")
fo.write('url_list = [')

url = "https://india.gov.in/my-government/schemes"
q = Request(url,headers=header)
response = urlopen(q)
if response.status == 200:
    soup = BeautifulSoup(response, "lxml")
    data = soup.select('#block-system-main > div > div.region.region-three-25-50-25-second > div > div.panel-pane.pane-views.pane-metadata-for-schemes.no-title.block > div > div > div > div.view-content > div > ul')
    data = data[0]
    links = data.findAll('a')
    for link in links:
        print(link.get_text())
        fo.write("'")
        fo.write('https://india.gov.in' + link['href'])
        fo.write("',")
        fo.write('\n')


for i in range(1,5):
    url = "https://india.gov.in/my-government/schemes?jurisdiction=All&ministry=All&field_st_dept_tid=All&title=&page=" + str(i)
    print(url)
    q = Request(url,headers=header)
    response = urlopen(q)
    if response.status == 200:
        soup = BeautifulSoup(response, "lxml")
        data = soup.select('#block-system-main > div > div.region.region-three-25-50-25-second > div > div.panel-pane.pane-views.pane-metadata-for-schemes.no-title.block > div > div > div > div.view-content > div > ul')
        data = data[0]
        links = data.findAll('a')
        for link in links:
            print(link.get_text())
            fo.write("'")
            fo.write('https://india.gov.in' + link['href'])
            fo.write("',")
            fo.write('\n')
			# url = 'https://india.gov.in' + link['href']
			# url_list.append(url)
    else:
        break
fo.write(']\nprint(url_list)')

# print(url_list)
# fo.write(str(url_list))
# fo.close()
