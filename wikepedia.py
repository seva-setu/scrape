from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import csv
import pandas as pd

wiki = "https://en.wikipedia.org/wiki/List_of_government_schemes_in_India"
header = {'User-Agent': 'Mozilla/5.0'}

q = Request(wiki)
q.add_header('User-Agent', 'Mozilla/5.0')
page = urlopen(q)
soup = BeautifulSoup(page,"html.parser")


data = {
	'_title' : [],
    'link' : [],
    'detail' : [],
    'ministry' : [],
    'sector' : []
}


table = soup.find("table", { "class" : "wikitable sortable" })



for row in table.findAll("tr"):
	cells = row.findAll("td")
    #For each "tr", assign each "td" to a variable.
	if len(cells) == 6:
		links_res = cells[0].findAll('a', href=True)
		for res in links_res:
			link = "https://en.wikepedia.org" + res.get('href')
			if '#' in link:
				link = ''

		title = cells[0].find(text=True)
		ministry = cells[1].find(text=True)
		sector = cells[4].find(text=True)   #to be added under benefits column
		detail = cells[5].find(text=True)


		data['_title'].append(title)
		data['link'].append(link)
		data['detail'].append(detail)
		data['ministry'].append(ministry)
		data['sector'].append(sector)


dogData = pd.DataFrame( data )
dogData.to_csv("sample2.csv")
