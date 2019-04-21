from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')
d.get('https://duckduckgo.com/')
d.find_element_by_id('search_form_input_homepage')
d.
