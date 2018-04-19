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
from selenium import webdriver
import cookielib
from middlewares import error_log, output_file, time_out, pagination_timeout

"""
Scraper functions for each ecommerce store
Start scraper options:

	1. Call the function scraper on a product category, eg: amazon_scraper('amazon.com/smartphones')
	2. Insert multiple product categories into a file urls.txt and run "python start_scraper.py"



"""

scrape_page_log = []
amazon_products_list = []
bestbuy_products_list = []
homedepot_products_list = []


def amazon_scraper(category_url):

	page_link = str(category_url)

	now=datetime.now()
	print ''
	#To avoid pages with pagination issues, check if the page wasn't scraped already
	if page_link not in scrape_page_log:
		#appends url to pages that are scraped
		scrape_page_log.append(page_link)	
		print 'Start scraping '+'Items: '+str(len(amazon_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+' Page: '+str(page_link)

		shop_page_req_head = urllib2.Request(page_link)
		shop_page_req_head.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0')
		#load page and create soup	
		shop_page = urllib2.urlopen(shop_page_req_head)
		shop_soup = BeautifulSoup(shop_page, 'html.parser')
		
		#get the domain of the url for exporting file name
		domain_url = tldextract.extract(page_link)
		#join to add also domain suffix link domain.com
		domain_name = '.'.join(domain_url[1:])
		file_name = domain_url.domain

		#DATA EXTRACTION
		#store all product divs from the page in a list
		items_div = shop_soup.find_all('div', {'class': 's-item-container'})
		
		#loop the scraped products list and extract the required data 
		for div in items_div:
			try:
				#check if current page is the first category page 
				if div.find('span', {'class': 'sx-price-whole'}):
					price = str(div.find('span', {'class': 'sx-price-whole'}).text.strip())
				else: 
					price = str(div.find('span', {'class': 'a-size-base a-color-base'}).text.strip())
				#verify if the product is rated
				if div.find('span', {'class': 'a-icon-alt'}):
					rating = str(div.find('span', {'class': 'a-icon-alt'}).text.strip())
				else:
					rating = 'Not rated yet'

				#append data in list of items
				amazon_products_list.append({
					'title' : div.find('a', {'class': 'a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal'})['title'], 
					'url' : div.find('a', {'class': 'a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal'})['href'], 
					'price' : str(price), 
					'rating' : str(rating),
					'domain' : domain_name})

				print div.find('a', {'class': 'a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal'})['title']

			except:
				pass			
					
			#random time delay 1 to several seconds (change 6 with the max seconds for delay)
			time_out(6)
		#END DATA EXTRACTION
		now=datetime.now()
		print 'Page completed '+'Items: '+str(len(amazon_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
		
		#PAGINATION AND CHANGING THE NEXT PAGE
		#check if current page is last for last page by reading the page button link	
		if shop_soup.find('a', {'id': 'pagnNextLink'}):

			#loads next page button link
			next_page_button = shop_soup.find('a', {'id': 'pagnNextLink'})['href']
			next_page_button_href = 'https://www.amazon.com' + str(next_page_button)
			#write scraped data to json file
			output_file(file_name, amazon_products_list)
			#change 5 to max seconds to pause before changing to next page
			pagination_timeout(5)
			amazon_scraper(next_page_button_href)
		else:
			#write scraped data to json file
			output_file(file_name, amazon_products_list)
			print 'Category Scraped Completed '+'Items: '+str(len(amazon_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
		#END PAGINATION	

	else:
		#logs pages issues such as missing next page button or infinit loops
		error_log(page_link, 'Pagination issues')
		print ''
		print 'ERROR! Page '+str(page_link)+' already scraped. See error log'
		output_file(file_name, amazon_products_list)
		print 'Category Scraped Completed '+'Items: '+str(len(amazon_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
		time.sleep(6)
		return

	return


def bestbuy_scraper(category_url):

	page_link = str(category_url)

	now=datetime.now()
	print ''
	#check if page was scraped already and start scraping if it wasn't
	if page_link not in scrape_page_log:
		#append page to log_[job_date].csv for not scraping it again during current job
		scrape_page_log.append(page_link)	

		print 'Start scraping '+'Items: '+str(len(bestbuy_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+' Page: '+str(page_link)

		#open browser for accessing the page - Bestbuy.com doesn't allow scraping without headers
		driver = webdriver.Firefox()
		#opens the page in browser
		driver.get(page_link)
		#creates the soup for scraping data
		html = driver.page_source
		shop_soup = BeautifulSoup(html, 'html.parser')
		
		#get the domain of the given page
		domain_url = tldextract.extract(page_link)
		#join to add also domain suffix link domain.com
		domain_name = '.'.join(domain_url[1:])
		file_name = domain_url.domain

		#store all product divs from the page in a list
		items_div = shop_soup.find_all('div', {'class': 'list-item'})

		#loop the scraped products list and extract the required data 
		for div in items_div:
			#check if product review exists		
			if div.find('div', {'span': 'c-review-average'}):
				rating = div.find('span', {'class': 'c-review-average'}).text.strip()
			elif div.find('span', {'class': 'c-reviews-none'}):
				rating = div.find('span', {'class': 'c-reviews-none'}).text.strip()
			else:
				rating = 'u/n'
			#get product title and url details
			if div.find('div', {'class': 'sku-title'}):
				product_info = div.find('div', {'class': 'sku-title'})
				product_title = product_info.text.strip()
				product_url = product_info.find('a', href=True)['href']
			#get price if present
			if div.find('div', {'class': 'pb-hero-price pb-purchase-price'}):
				#get price and remove the $ sign before the actual price
				price = str(div.find('div', {'class': 'pb-hero-price pb-purchase-price'}).text.strip())[1:]
			else:
				price = 'u/n'
			
			#append all data to product list			
			bestbuy_products_list.append({
				'title' : product_title,
				'url' : 'https://www.bestbuy.com' +str(product_url), 
				'price' : price, 
				'rating' : rating,
				'domain' : domain_name})

			print product_title
			
			#random time delay 1 to several seconds
			time_out(6)

		now=datetime.now()
		print 'Page completed '+'Items: '+str(len(bestbuy_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
				
		#get pagination div to change page or stop job	
		if shop_soup.find('div', {'class': 'results-pagination'}):
			#extract the chevron tiles for previous and next page
			next_page_click = shop_soup.find_all('a', {'class': 'btn btn-primary btn-sm btn-ficon '})
			
			#nxt page is the second and last item and it compares the last digit with current page digits to check if there is a next page
			while next_page_click[-1]['href'][-1] > page_link[-1]:
				try:		
					next_page_button_href = next_page_click[-1]['href']		
					#write scraped data to json file
					output_file(file_name, bestbuy_products_list)
					pagination_timeout(5)	
					#close browser window
					driver.quit()
					bestbuy_scraper(next_page_button_href)	
					break
				except:
					break

			else:
				#write scraped data to json file
				output_file(file_name, bestbuy_products_list)
				driver.quit()
				print 'Category Scraped Completed '+'Items: '+str(len(bestbuy_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
				
	else:
		#appends any page with issues to log_error_[job_date].csv
		error_log(page_link, 'Pagination issues')
		print ''
		print 'ERROR! Page '+str(page_link)+' already scraped. See error log'
		output_file(file_name, bestbuy_products_list)
		driver.quit()
		print 'Category Scraped Completed '+'Items: '+str(len(bestbuy_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
		time.sleep(6)
		return
	return


def homedepot_scraper(category_url):
	
	page_link = str(category_url)

	now=datetime.now()
	print ''
	#To avoid pages with pagination issues, check if the page wasn't scraped already
	if page_link not in scrape_page_log:
		#appends url to pages that are scraped
		scrape_page_log.append(page_link)	
		print 'Start scraping '+'Items: '+str(len(homedepot_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+' Page: '+str(page_link)

		shop_page_req_head = urllib2.Request(page_link)
		shop_page_req_head.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0')
		#load page and create soup	
		shop_page = urllib2.urlopen(shop_page_req_head)
		shop_soup = BeautifulSoup(shop_page, 'html.parser')
		
		#get the domain of the url for exporting file name
		domain_url = tldextract.extract(page_link)
		#join to add also domain suffix link domain.com
		domain_name = '.'.join(domain_url[1:])
		file_name = domain_url.domain

		#DATA EXTRACTION
		#store all product divs from the page in a list
		items_div = shop_soup.find_all('div', {'class': 'pod-inner'})
		
		#loop the scraped products list and extract the required data 

		for div in items_div:	
			try:
				#append data in list of items
				homedepot_products_list.append({
					'title' : div.find('div', {'class': 'pod-plp__description js-podclick-analytics'}).text.strip(), 
					'url' : 'https://www.homedepot.com'+str(div.find('a', {'class': 'js-podclick-analytics'})['href']), 
					'price' : div.find('div', {'class': 'price'}).text.strip()[1:-2], 
					'domain' : domain_name})

				print div.find('div', {'class': 'pod-plp__description js-podclick-analytics'}).text.strip()
			except:
				pass			
					
			#random time delay 1 to several seconds (change 6 with the max seconds for delay)
			time_out(6)
		#END DATA EXTRACTION
		now=datetime.now()
		print 'Page completed '+'Items: '+str(len(homedepot_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)

		#PAGINATION 
		#check if current page is last for last page by reading the page button link	
		if shop_soup.find('li', {'class': 'hd-pagination__item hd-pagination__button'}):

			#loads next page button link
			next_page_click = shop_soup.find_all('a', {'class': 'hd-pagination__link'})
			while next_page_click[-1]['title'] == 'Next':
				next_page_button_href = 'https://www.homedepot.com'+str(next_page_click[-1]['href'])
				try:
					#write scraped data to json file
					output_file(file_name, homedepot_products_list)
					#change 5 to max seconds to pause before changing to next page
					pagination_timeout(5)
					homedepot_scraper(next_page_button_href)
					break
				except:
					break
			else:
				#write scraped data to json file
				output_file(file_name, homedepot_products_list)
				print 'Category Scraped Completed '+'Items: '+str(len(homedepot_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
			#END PAGINATION	
	else:
		#appends any page with issues to log_error_[job_date].csv
		error_log(page_link, 'Pagination issues')
		print ''
		print 'ERROR! Page '+str(page_link)+' already scraped. See error log'
		output_file(file_name, homedepot_products_list)
		print 'Category Scraped Completed '+'Items: '+str(len(homedepot_products_list))+' At: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
		time.sleep(6)
		return
	return
