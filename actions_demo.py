from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://google.com')

#locate  teh search box element

search_box = driver.find_element_by_name('q')

import time
time.sleep(5)

# type in search query
search_box.send_keys('seleniumhq'+ Keys.RETURN)

time.sleep(5)

print(driver.title)

driver.quit()
