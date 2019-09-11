import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy as np

'''
Scrap wiki articles for information concerning labels
'''


# file with kpop artists
f = open("kpop_wiki_urls.csv")
lines = f.readlines() # skip header

urls = []

for i in lines:
    i = i.rstrip("\n\r")
    url = ('https://en.wikipedia.org%s' % i)
    urls.append(url)
f.close()

# print(urls)

artist_labels = {}
failed_searches = []

for url in urls: 
    artist_name = url.replace('https://en.wikipedia.org/wiki/', '')
    
    # Scraping wikipedia for background information tables
    website_url = requests.get(url).text

    soup = BeautifulSoup(website_url,'lxml')

    # get the background info table
    table = soup.find('table', {'class':'infobox vcard plainlist'})

    labels = []
    print(artist_name)

    if not table:
        failed_searches.append(artist_name)
        continue

    for div_class in table.find_all("tr"):
        if "Labels" in div_class.text:
            # print(div_class) # the entire line
            # print(div_class.prettify())
            # multiple types of tags flank the label info
            for i in div_class.findAll(['li', 'a']):
                labels.append(i.text)
            # lab_string = div_class.text
            # print(lab_string)
            # print(lab_string.lstrip('Labels'))
        
    artist_labels[artist_name] = labels

# print(artist_labels)

#print out label info
w = csv.writer(open('kpop_wiki_labelinfo.csv', 'w'))
for key, val in artist_labels.items():
    w.writerow([key, val])

failed_search_df = pd.DataFrame(failed_searches) 
failed_search_df.to_csv('Failed_Searches_wiki_labelinfo.csv') #file with the failed queries