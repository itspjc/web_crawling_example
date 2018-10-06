from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

path_chrome_driver = "./chromedriver"
url = "https://www.beeradvocate.com/"

driver = webdriver.Chrome(path_chrome_driver)
driver.get(url)

# driver.find_element_by_id("lst-ib").send_keys("selenium")
# driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」と一致するリンクをクリックする。
# driver.find_element_by_link_text("Selenium - Web Browser Automation").click()


sleep(5)
driver.close()
