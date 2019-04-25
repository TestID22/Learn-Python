from selenium import webdriver
import time 

webdriver = webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
webdriver.get('https://habr.com/ru/post/250921/')
print(webdriver.find_element_by_tag_name('h1').text)