# coding utf-8
from selenium import webdriver

driver = webdriver.Chrome() #从https://sites.google.com/a/chromium.org/chromedriver/downloads下载chromeDrive
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys('selenium2')
driver.find_element_by_id("su").click()
driver.quit()