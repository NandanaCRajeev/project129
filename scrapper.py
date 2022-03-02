from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

url ='https://en.wikipedia.org/wiki/List_of_brown_drawns'
page=requests.get(url)
soup=bs(page.text,'html.parser')
star_table=soup.find_all('table')
table_rows=star_table[7].find_all('tr')