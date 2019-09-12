import requests
from bs4 import BeautifulSoup
import re

'''
Get the end of the urls for kpop artists on the two wikipedia list pages with Beautiful Soup!!!
Sept 10
'''
# websites I want to scrap
website_urls = ['https://en.wikipedia.org/wiki/List_of_South_Korean_idol_groups_(2000s)', 'https://en.wikipedia.org/wiki/List_of_South_Korean_idol_groups_(2010s)']

for url in website_urls: 
    website_url = requests.get(url).text

    soup = BeautifulSoup(website_url,'lxml')

    url_list = []

    # headers of the sections I want to scrape from 
    years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

    for year in years:
        for headline in soup.findAll('span', {'class':'mw-headline', 'id':year}):
            # print(headline)
            links = headline.find_next('ul').find_all('a')
            for link in links:
                # print(link.get('href'))
                if link.get('href').startswith('/wiki/'):
                    url_list.append(link.get('href'))

# print(url_list)
        
# Save scraped URLS to file
with open('kpop_wiki_urls.csv', 'w') as filehandle:
    for item in url_list:
        filehandle.write('%s\n' % item)

