import time
from selenium import webdriver

driver =webdriver.Chrome('C:/Users/phili/Documents/Jun Docs/ChromeDriver/chromedriver')
driver.get('https://www.seleniumhq.org')

print (driver.title)

time.sleep (20)

driver.quit