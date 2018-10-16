import requests
from bs4 import BeautifulSoup
url = "https://www.yahoo.co.jp"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
# http://www.useragentstring.com/pages/useragentstring.php
response = requests.get(url, headers=headers)
text = response.text

soup = BeautifulSoup(text, "html.parser")
news_box = soup.find("div", {"id": "topicsfb"})
for item in news_box.find_all("li"):
	print (item.a.get_text())




