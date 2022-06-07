from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from bs4 import BeautifulSoup
#import pandas

#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
i = "test"
driver.get(f"https://thepiratebay.org/search.php?q={i}")
driver.find_element(By.ID, "torrents")
#data = pandas.read_html(driver.page_source)
#print(data)
## this right here is the sauce
soup = BeautifulSoup(driver.page_source, 'lxml')
table = soup.find('ol')
data = []
for listings in table.find_all('li'):
    data+=listings.get_text().strip().split('\n ')
print(data)




#span = []
#for listing in soup.find_all('li'):
#   for items in listing:
#       span += items.get_text().strip('').split('\n')
#print(span)


#print(span)
#newDict = {}
#span_dict = {k: v for v, k in enumerate(span)}
#print(span_dict)
# This is to filter out entries by their key, as span returns all items, but
# I would like them organized, an remove any not needed.
# Just do the math for the ones you want in new Dict next time you are playing
# around. Current as of 05/06 15:05 is just placeholder
#for (k, v) in span_dict.items():
#   if int(v) % 2 == 0:
#       newDict[k] = v
#print(newDict)
#
#
#
