#!/usr/bin/python

"""
	### BEAGLE SCRAPER ###

	### The product category scraper ###
	
"""

import beagle_scraper as scrape
import urllib2
from bs4 import BeautifulSoup
import tldextract
from datetime import datetime, date
import time
import csv
from middlewares import error_log, output_file, scrape_log

"""
Open links from a text file and feeds it to the scraper

USAGE:
	1. Paste prduct category links in a file "urls.txt"
	2. Run: python start_scraper.py
"""

today = datetime.now()
directory = str(today.day)+'_'+str(today.strftime("%b")).lower()+'_'+str(today.year)

print 'Opening: urls.txt'
time.sleep(3)

with open('urls.txt') as links_file:
	links = links_file.readlines()

#Get each url from url.txt to start scraping job
for category_url in links:
	
	category_url = str(category_url)
	#get the domain of a link from given list
	domain_name = tldextract.extract(category_url)
	#join to add also domain suffix link domain.com
	domain_ext = '.'.join(domain_name[1:])
	
	print 'Start scraper for ' + str(domain_ext)
	time.sleep(2)

	if domain_ext == 'amazon.com':
		try:
			scrape.amazon_scraper(category_url)
			pass
		except:
			pass

	if domain_ext == 'bestbuy.com':
		try:
			scrape.bestbuy_scraper(category_url)
			pass
		except:
			pass

	if domain_ext == 'homedepot.com':
		try:
			scrape.homedepot_scraper(category_url)
			pass
		except:
			pass


	else:
		print 'No scraper for domain: ' + str(domain_name.domain)
		print ''

	#log the last link accessed, either scraped or not
	scrape_log(category_url)
