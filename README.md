# Beagle Scraper

Building the largest open-source Ecommerce scraper with Python and BeautifulSoup4

## Usage

No installation or setup required

1. Download the source code into a folder
2. Create a **urls.txt** file with product category pages to be scraped like this [Amazon page](https://www.amazon.com/TVs-HDTVs-Audio-Video/b/ref=tv_nav_tvs?ie=UTF8&node=172659&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=WQG6T4RDNW1YMS15T8Q8&pf_rd_r=WQG6T4RDNW1YMS15T8Q8&pf_rd_t=101&pf_rd_p=2905dcbf-1f2a-4de6-9aa1-c71f689a0780&pf_rd_p=2905dcbf-1f2a-4de6-9aa1-c71f689a0780&pf_rd_i=1266092011)
3. Run the command
```
$ python start_scraper.py
```

### Output

Beagler Scraper will export all data into JSON format into a sub-folder

## Current supported e-commerce stores

* Amazon.com
* BestBuy.com
* HomeDepot.com

### Beagle Scraper tutorial - how to use and run the scraper

https://www.bestproxyproviders.com/blog/beagle-scraper-tutorial-how-to-scrape-e-commerce-websites-and-modify-the-scraper/

## Getting Started

Beagle Scraper requires a machine with Python 2.7 and BeautifulSoup4

Install BeautifoulSoup4
```
$ pip install beautifulsoup4
```

### Prerequisites - extra Python packages required

The following packages are not included in the default Python 2.7 install and require installation

* tldextract
```
$ sudo pip install tldextract
```
* selenium
```
$ pip install selenium
```
If another package is missing run the command

```
$ pip install [missing package name]
```

## Using proxies to scrape

Beagle Scraper support external proxies at the moment, but [proxychains](https://github.com/haad/proxychains) can be used to send requests through different proxies

After installing proxychains, run this command to make the scraper use proxies
```
$ proxychains python start_scraper.py
```

## Test Beagle Scraper

Here's a short test for Beagle Scraper

1. Download Beagle Scraper
2. Create a **urls.txt** file and insert the following product category pages (each link on a different line)

* https://www.amazon.com/TVs-HDTVs-Audio-Video/b/ref=tv_nav_tvs?ie=UTF8&node=172659&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=WQG6T4RDNW1YMS15T8Q8&pf_rd_r=WQG6T4RDNW1YMS15T8Q8&pf_rd_t=101&pf_rd_p=2905dcbf-1f2a-4de6-9aa1-c71f689a0780&pf_rd_p=2905dcbf-1f2a-4de6-9aa1-c71f689a0780&pf_rd_i=1266092011
* https://www.bestbuy.com/site/tvs/75-inch-tvs/pcmcat1514910595284.c?id=pcmcat1514910595284

3. Run Beagle Scraper

```
$ python start_scraper.py
```
Example output for the above scraped urls:

* amazon_dd_mm_yy.json
* bestbuy_dd_mm_yy.json


## Built With

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Scraping library
* [Python 2.7](https://www.python.org/) - Dependency Management

## How to contribute

All you have to do is to create a function scraper link **amazon_scraper()** from [beagle_scraper.py](https://github.com/ChrisRoark/beagle_scraper/blob/master/beagle_scraper.py) and submit it here.

Here is more info on how the scraper function is created

Things to consider:
1. HTML wrapper and class/id for each product listed on the page
2. The product details HTML tags and classes
3. Pagination setup

## Authors

* **Chris Roark** - *Initial work* - [ChrisRoark](https://github.com/ChrisRoark)

## License

GPL-3.0 license
