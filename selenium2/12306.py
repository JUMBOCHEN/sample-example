#date 2018.1.3
#author chenzuobao
'''
webdriver  Chrome谷歌浏览器驱动，
selenium2  自动化测试框架，
Chrome插件Xpath Helper可以方便定位元素，
'''

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.12306.cn/mormhweb/")
'''
driver.find_element_by_class_name("k2").click()
driver.find_element_by_id("login_user").click()
driver.find_element_by_id("username").send_keys("never641724352")
driver.find_element_by_id("password").send_keys("czb641724352")
'''
cookies = driver.get_cookies()
print(cookies)
driver.quit()
