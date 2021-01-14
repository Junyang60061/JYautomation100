from selenium import webdriver
from locators import WikipediaHomepage, WikipediaArticle
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/Users/phili/Documents/Jun Docs/Selenium/chromedriver')
driver.get('https://en.wikipedia.org')

random_link = driver.find_element(*WikipediaHomepage.Random_link)
random_link.click()

time.sleep(5)

first_heading = driver.find_element(*WikipediaArticle.First_heading)
print(first_heading.text)

page_info = driver.find_element(*WikipediaArticle.Page_info)
page_info.click()
time.sleep(5)
search_box = driver.find_element(*WikipediaArticle.Search_box)
search_box.send_keys('Selenium (software)' + Keys.RETURN)

time.sleep(5)

Logo= driver.find_element(*WikipediaArticle.Logo)
Logo.click()
time.sleep(5)

driver.quit()