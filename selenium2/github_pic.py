#author chenzuobao
#date   2017.12.20
#用selenium2自动登陆GitHub并把contribute截图出来。
# 每天看点亮的contributes,.....哈哈哈哈

# coding utf-8
from selenium import webdriver
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.find_element_by_id("login_field").send_keys("JUMBOCHEN")
driver.find_element_by_id("password").send_keys("Gan796489321")
driver.find_element_by_class_name("btn").click()
driver.get("https://github.com/JUMBOCHEN")
text = str(datetime.now())
print(text)
driver.get_screenshot_as_file("D:\\Python\\github每日一图\\"+text[:10]+".png")
driver.quit()

# successful~
#最后用pyinstaller打包成EXE