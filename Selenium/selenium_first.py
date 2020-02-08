from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

d = webdriver.Chrome(r'D:\driver\chromedriver')
d.get('https://duckduckgo.com/')
element = d.find_element_by_class_name('search-wrap--home')
time.sleep(5)
element.send_keys("123")