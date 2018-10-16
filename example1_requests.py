
import requests
url = "https://www.yahoo.co.jp"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
response = requests.get(url, headers=headers) 

text = response.text
print (text)




# http://www.useragentstring.com/pages/useragentstring.php
#response = requests.get(url)





