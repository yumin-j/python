from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import bs4
# soup = bs4.BeautifulSoup()
# from bs4 import BeautifulSoup
# soup = BeautifulSoup()->>>bs4안써도 from을 사용하면 이렇게 사용할 수 있다.

# import selenium을 해줬겠지만 위에 프롬을 했기 때문에 다음만 해도
#.:현재드라이버
path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.google.com/')
search_input = driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
search_input.send_keys('hello world') 
search_input.send_keys(Keys.RETURN)