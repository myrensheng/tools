import random
import time
from selenium import webdriver
from lxml import html
url = 'http://bhtg.baihe.com/stat.html?ggCode=zhuceyouhua_3#http://my.baihe.com/login'
browser = webdriver.Chrome()
browser.get(url)
try:
    time.sleep(random.randint(2,5))
    browser.find_element_by_id('txtLoginEMail').send_keys('17794032575')
    browser.find_element_by_xpath('//*[@id="txtLoginPwdRepeat"]').click()
    time.sleep(random.randint(2,5))
    # js = "document.getElementById('txtLoginPwdRepeat').style.display='block';"
    # browser.execute_script(js)
    time.sleep(random.randint(2,5))
    browser.find_element_by_xpath('//*[@id="txtLoginPwdRepeat"]').send_keys('17794032575')
    browser.find_element_by_class_name('btn').click()
except Exception as e:
    print(e)
    browser.quit()
