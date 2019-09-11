import requests
from bs4 import BeautifulSoup

# # file with kpop artists
# f = open("kpop_groups_2000_2019.csv")
# lines = f.readlines()[1:] # skip header

# artists = []
# urls = []

# for x in lines:
#     artist_name = x.split(",")[0]
#     artist_name = artist_name.replace(' ', '_')
#     url = ('https://en.wikipedia.org/wiki/%s' % artist_name)
#     urls.append(url)
# f.close()

# print(urls)

# Scraping wikipedia for background information tables
website_url = requests.get('https://en.wikipedia.org/wiki/Uniq').text

soup = BeautifulSoup(website_url,'lxml')

artist_labels = {}
# get the background info table
table = soup.find('table', {'class':'infobox vcard plainlist'})

labels = []

for div_class in table.find_all("tr"):
    if "Labels" in div_class.text:
        # print(div_class) # the entire line
        # print(div_class.prettify())
        for i in div_class.findAll('li'):
            labels.append(i.text)
        # lab_string = div_class.text
        # print(lab_string)
        # print(lab_string.lstrip('Labels'))


artist_labels[artist_names] = labels