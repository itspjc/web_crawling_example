from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

path_chrome_driver = "./chromedriver"
url = "https://www.beeradvocate.com/"

driver = webdriver.Chrome(path_chrome_driver)
driver.get(url)


sleep(5)
driver.close()
