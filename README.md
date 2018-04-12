# Beagle Scraper

Building the largest open-source Ecommerce and listing pages scraper in Python and BeautifulSoup4

## Getting Started

Beagle Scraper requires a machine with Python 2.7 and BeautifulSoup4

Install BeautifoulSoup4
```
$ pip install beautifulsoup4
```

### Prerequisites - extra Python packages required

The following packages are not included in the default Python 2.7 install and require installation.

* tldextract
```
sudo pip install tldextract
```
* selenium
```
pip install selenium
```
If another package is missing run the command

```
$ pip install [missing package name]
```

### Usage

No install or setup required.

1. Download the files into a folder
2. Create a urls.txt file with product category pages to be scraped like this one
* https://www.amazon.com/s/ref=lp_283155_nr_n_0?fst=as%3Aoff&rh=n%3A283155%2Cn%3A%211000%2Cn%3A1&bbn=1000&ie=UTF8&qid=1523546751&rnid=1000
3. Run the command
```
$ python start_scraper.py
```

### Output

Beagler Scraper will export all data into json format in the folder where the Python files are saved. 


## Using proxies to scrape

Beagle Scraper doesn't support proxies at the moment, but proxychains can be used to send request through different proxies.

### Install proxychains

* [How to install proxychains]()

After installing proxychains, run this command to make the scraper use proxies
```
$ proxychains python start_scraper.py
```



## Test Beagle Scraper

Here's a short test for Beagle Scraper

1. Download Beagle Scraper
2. Create a urls.txt file and insert the following product categody pages (each link on a different line)

* https://www.amazon.com/s/ref=lp_283155_nr_n_0?fst=as%3Aoff&rh=n%3A283155%2Cn%3A%211000%2Cn%3A1&bbn=1000&ie=UTF8&qid=1523546751&rnid=1000
* https://www.bestbuy.com/site/tvs/75-inch-tvs/pcmcat1514910595284.c?id=pcmcat1514910595284

3. Run Beagle Scraper

```
$ python start_scraper.py
```
Example output for the above scraped urls:

amazon_dd_mm_yy.json
bestbuy_dd_mm_yy.json


## Built With

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Scraping library
* [Python 2.7](https://www.python.org/) - Dependency Management

## How to contribute

Everybody is welcomed in contributing. 

All you have to do is to create a function scraper link **amazon_scraper()** from [beagle_scraper.py](https://github.com/ChrisRoark/beagle_scraper/blob/master/beagle_scraper.py) and submit it here.

Things to consider:
1. HTML wrapper and class/id for each product listed on the page
2. The product details HTML tags and classes
3. Pagination setup

## Authors

* **Chris Roark** - *Initial work* - [ChrisRoark](https://github.com/ChrisRoark)
