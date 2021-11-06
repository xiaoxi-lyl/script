from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
chrome_options.add_argument('--headless')         # 无头浏览器
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='D:\Google\Chrome\Application\chromedriver.exe', chrome_options=chrome_options)
driver.get('http://10.255.200.11/portal/index.html?v=202103260001')
time.sleep(0.5)
driver.find_element_by_id("username").send_keys("学号")   # 用户名
driver.find_element_by_id("password").send_keys("密码")                # 密码
select = Select(driver.find_element_by_name("domain"))
select.select_by_value('cmcc')              # 移动用户
select.select_by_value('telecom')           # 电信用户
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()  #点击登录
driver.quit()

