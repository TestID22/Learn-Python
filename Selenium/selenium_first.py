from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

d = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver')
d.get('https://duckduckgo.com/')
d.find_element_by_id('search_form_input_homepage')
time.sleep(5)
d.send_keys_to_element('sss')