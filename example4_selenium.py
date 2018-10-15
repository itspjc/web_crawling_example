from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#path_chrome_driver = "C:/selenium/chromedriver.exe"
path_chrome_driver = "./chromedriver"
url = "https://www.yahoo.co.jp"

driver = webdriver.Chrome(path_chrome_driver)
driver.get(url)
search_text = "プーと大人になった僕"
driver.find_element_by_xpath('//*[@id="srchtxt"]').send_keys(search_text)
sleep(2)
driver.find_element_by_id('srchbtn').click()
test = driver.find_element_by_xpath(
    '//*[@id="sIn"]/div/div[2]/ul/li[1]/a').text
print(test)
sleep(5)
driver.close()

# driver.find_element_by_id("lst-ib").send_keys("selenium")
# driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
# driver.find_element_by_link_text("Selenium - Web Browser Automation").click()
