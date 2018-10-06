import requests
import csv
from bs4 import BeautifulSoup
url = "https://www.beeradvocate.com/beer/"
response = requests.get(url)
text = response.text

soup = BeautifulSoup(text, "html.parser")

# a = soup.find("h6")
# print(a)

with open('beer_list.csv', 'w') as output:
    writer = csv.writer(output, delimiter=',', lineterminator='\n')
    writer.writerow(["name", "rate"])

    for item in soup.find_all("div", {"id": "rating_fullview_container"}):
        beer_name = item.h6.a.get_text()
        beer_rate = item.find("span", {"class": "BAscore_norm"}).get_text()
        writer.writerow([beer_name, beer_rate])
        print([beer_name, beer_rate])
