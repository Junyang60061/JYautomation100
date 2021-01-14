from selenium.webdriver.common.by import By 

class WikipediaHomepage(object):
	Random_link = (By.CSS_SELECTOR, '#n-randompage')


class WikipediaArticle(object):
	First_heading =(By.CSS_SELECTOR,'.firstHeading')
	Page_info =(By.LINK_TEXT, 'Page information')
	Search_box=(By.NAME, 'search')
	Logo =(By.XPATH, '/html/body/div[5]/div[2]/div/a')
