# coding utf-8
from selenium import webdriver

driver = webdriver.Chrome() #从https://sites.google.com/a/chromium.org/chromedriver/downloads下载chromeDrive
driver.get("http://www.baidu.com")
text = driver.find_element_by_id("cp").text
print(text)
driver.find_element_by_id("kw").send_keys('selenium2')
driver.find_element_by_id("su").click()
for list1 in range(1, 10):
    driver.refresh()
driver.quit()