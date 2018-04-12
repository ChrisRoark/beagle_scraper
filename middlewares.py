"""
	### BEAGLE SCRAPER ###

	### The product category scraper ###
	
"""
import urllib2
from bs4 import BeautifulSoup
import csv
import json
import re
from random import randint
import time
from datetime import datetime, date
import os
import tldextract

"""
Functions use in scrapers
"""


#log the last link accessed, either scraped or not
def scrape_log(open_link):

	now=datetime.now()
	today = date.today()
	directory = str(today.day)+'_'+str(today.strftime("%b")).lower()+'_'+str(today.year)
	
	if not os.path.exists(directory):
		os.makedirs(directory)

	logged_link = str(open_link)[:-1]
	log_csv = str(today), str(now.hour)+':'+str(now.minute)+':'+str(now.second),logged_link
	log_file = open(str(directory)+'/log_'+str(directory)+'.csv', 'a')
	with log_file:
		writer = csv.writer(log_file)
		writer.writerow(log_csv)
	return

#logs errors into log_error_[job_date].csv file
def error_log(url, error_message):
	now=datetime.now()
	today = date.today()

	#creates folder to save scraped data for today
	directory = 'job_'+str(today.day)+'_'+str(today.strftime("%b")).lower()+'_'+str(today.year)
	if not os.path.exists(directory):
		os.makedirs(directory)

	logged_link = str(url)
	error_type = str(error_message)
	error_csv = [str(today), str(now.hour)+':'+str(now.minute)+':'+str(now.second),str(logged_link),str(error_type)]
	error_file = open(str(directory)+'/log_error_'+str(directory)+'.csv', 'a')
	with error_file:
		writer = csv.writer(error_file)
		writer.writerow(error_csv)
	return

def output_file(domain, products_list):
	print "Exporting your products to file"
	today = datetime.now()

	#creates folder to save scraped data for today
	directory = 'job_'+str(today.day)+'_'+str(today.strftime("%b")).lower()+'_'+str(today.year)
	if not os.path.exists(directory):
		os.makedirs(directory)

	output_file_json = str(directory)+'/'+str(domain) + '_products_'+str(directory)+'.json'
	with open(output_file_json, 'w') as outfile:		
		json.dump(products_list, outfile)
	return

def time_out(seconds):
	#timeout during scraping job - assign preffered max seconds for pausing the scraper
	max_timeout = int(seconds)
	print "Timeout for a few seconds..."
	time.sleep(randint(2,max_timeout))
	return

def pagination_timeout(seconds):
	#timeout for scraper after scraping one page and before moving to another
	print "Changing the page, please wait a few seconds..."
	max_timeout = int(seconds)
	time.sleep(randint(2,max_timeout))
	return