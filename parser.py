import csv
from bs4 import BeautifulSoup
import requests

filename = 'locatii.csv'
filename1 = 'pretty.txt'
f1 = open(filename1, 'w', encoding='utf-8')
f = open(filename, 'w', encoding='utf-8')
page_url = requests.get('https://ro.wikipedia.org/wiki/List%C4%83_de_localit%C4%83%C8%9Bi_din_jude%C8%9Bul_V%C3%A2lcea')
# print(page_url.status_code)
soup = BeautifulSoup(page_url.text, 'html.parser')
headers = 'locatii'
f.write(headers)
f1.write(soup.prettify())
a = soup.body.find_all('a')

table = soup.find_all('td') # it gives the first element of tbody->tr->td
for one in table[::3]:
    f.write(','+ one.text)
# print(table)

print('SUCCESS')