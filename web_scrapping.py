import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_text = requests.get(url).text
s = BeautifulSoup(url_text, 'html.parser')
# print(s.prettify())
# print(s.title)
# print(s.title.string)
tag = s.find_all('a')
# print(tag)
table = s.find_all('table')
# print(table)
my_table = s.find('table', class_='wikitable sortable plainrowheaders')
table_links = my_table.find_all('a')
print(table_links)
actors = []
for links in table_links:
    actors.append(links.get('title'))
print(actors)