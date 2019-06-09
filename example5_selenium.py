from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import codecs

# Windowsの場合
path_chrome_driver = "C:/selenium/chromedriver.exe"


# Macなどの場合
# path_chrome_driver = "./chromedriver"
url = "https://www.amazon.co.jp"

book_list_file = codecs.open('book_list.csv', 'r', 'utf-8')
output = codecs.open('output2.csv', 'w', 'utf-8')
first_line = book_list_file.readline()  # Skip Header
first_line = first_line.replace('\n', '').replace('\r', '')
output.write(first_line + ',' + 'genre' + '\n')

print('*** 書籍ジャンルクローリング実行 ***')

driver = webdriver.Chrome(path_chrome_driver)
driver.get(url)


for line in book_list_file:
    line = line.replace('\n', '').replace('\r', '').split(',')
    print('書籍名 ' + line[0])
    print('ISBNコード ' + line[1])
    search_isbn_code = line[1]

    dropdown_box = driver.find_element_by_id('searchDropdownBox')
    Select(dropdown_box).select_by_value('search-alias=stripbooks')
    driver.find_element_by_id(
        'twotabsearchtextbox').send_keys(search_isbn_code)
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="nav-search"]/form/div[2]/div').click()

    sleep(2)
    genre_text = driver.find_element_by_xpath(
        '//*[@id="leftNavContainer"]/ul[1]/ul/div/li[1]/span/a').text
    print(genre_text)
    output.write(line[0] + ',' + line[1] + ',' + genre_text + '\n')

    driver.get(url)
    # driver.find_element_by_xpath('//*[@id="srchtxt"]').send_keys(search_text)
    # sleep(2)
    # driver.find_element_by_id('srchbtn').click()
    #test = driver.find_element_by_xpath('//*[@id="sIn"]/div/div[2]/ul/li[1]/a').text

sleep(5)
driver.close()

# driver.find_element_by_id("lst-ib").send_keys("selenium")
# driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
# driver.find_element_by_link_text("Selenium - Web Browser Automation").click()
