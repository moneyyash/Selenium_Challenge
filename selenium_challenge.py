# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:57:28 2021

@author: LENOVO
"""

from selenium import webdriver
import time 
import requests
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://sdsclub.com');
time.sleep(5)

button_1= driver.find_element_by_xpath('/html/body/header/div/div/div[2]/nav/ul/li[1]/a').click()
time.sleep(5)

button_2 = driver.find_element_by_xpath("//*[@id='category-career']/div/div[2]/div[2]/div/figure/a/img").click()

time.sleep(10)
button_close = driver.find_element_by_class_name('close-icon').click()
time.sleep(5)

page_src = driver.page_source
soup =  BeautifulSoup(page_src, 'lxml')


scrape_1 = [i.text for i in soup.findAll('span', {'class': 'desc'})]
scrape_2 = [i.text for i in soup.findAll('div', {'class': 'single-path-article-content'})]
scrape_3= [i.text for i in soup.findAll('p', {'class': 'name'})]


df = pd.DataFrame(scrape_1)
df_2 = pd.DataFrame(scrape_2)
df_3 = pd.DataFrame(scrape_3)


print(df)
print(df_2)
print(df_3)

time.sleep(10)

driver.quit()








