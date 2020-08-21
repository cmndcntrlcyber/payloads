#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = 'http://dev.sneakycorp.htb/team.php'

with requests.Session() as req:
	r = req.get(url)
	html = r.text

	soup = BeautifulSoup(html, 'html.parser')
	data = soup.find_all('table',id='dataTable')
	for d in data:
		for number in range(3,231,4):
			emails = d.find_all('td')[number]
			for email in emails:
				print(email)
