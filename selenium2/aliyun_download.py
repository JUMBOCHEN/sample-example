# author chenzuobao
# date 2018.1.6
# 下载2017云栖大会干货  http://click.aliyun.com/m/38596/
# 基于selenium2

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(
    "https://passport.alibaba.com/mini_login.htm?lang=zh_CN&appName=aliyun&appEntrance=aliyun&styleType=vertical&bizParams=&notLoadSsoView=&notKeepLogin=true&isMobile=false&regUrl=https%3A%2F%2Faccount.aliyun.com%2Fregister%2Fregister.htm%3Fspm%3D5176.100238.765261.7.4b8421e5MF4E3Q%26qrCodeFirst%3Dfalse%26oauth_callback%3Dhttps%253A%252F%252Fyq.aliyun.com%252F&qrCodeFirst=false&returnUrl=https%3A%2F%2Faccount.aliyun.com%3A443%2Flogin%2Flogin_aliyun.htm%3Foauth_callback%3Dhttps%253A%252F%252Fyq.aliyun.com%252F&rnd=0.5714334365985285")
driver.find_element_by_id("fm-login-id").send_keys("风舞小子007")
driver.find_element_by_id("fm-login-password").send_keys("gan796489321")
driver.find_element_by_id("login-submit").click()

driver.get("http://click.aliyun.com/m/38596/")
driver.quit()
