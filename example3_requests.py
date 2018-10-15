import requests
import csv
import codecs
from bs4 import BeautifulSoup
url = "https://www.beeradvocate.com/beer/"
response = requests.get(url)
text = response.text

# 読み込んだHTML DOMを分解しやすくするため、BeautifulSoupを読み込む。
soup = BeautifulSoup(text, "html.parser")

fout = codecs.open('output.csv', 'w', 'utf-8')
fout.write("beer_name" + "," + "beer_rate" + "\n")
for item in soup.find_all("div", {"id": "rating_fullview_container"}):
    beer_name = item.h6.a.get_text()
    beer_rate = item.find("span", {"class": "BAscore_norm"}).get_text()
    fout.write(beer_name + "," + beer_rate + "\n")
    print([beer_name, beer_rate])
