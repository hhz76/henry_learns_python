from __future__ import unicode_literals
from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.escapeatx.com"

def get_deals(section_url):
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	deal = soup.find("div", "excerpt-header")
	content = [h1.get_text() for h1 in soup.findAll("h1", "excerpt-title")]
	return content

all_deals = get_deals(BASE_URL)

deals_file = open("deals.txt","w")

for link in all_deals:
	deals_file.write(link.encode('utf-8'))

deals_file.close()"# henry_learns_python" 
