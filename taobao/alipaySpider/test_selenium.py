# 测试selenium无界面浏览器能否截屏
# 可以截屏，但是好像比较小
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.save_screenshot("baidu2.png")
