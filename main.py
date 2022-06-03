from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from bs4 import BeautifulSoup

#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
i = "test"
driver.get(f"https://thepiratebay.org/search.php?q={i}")
driver.find_element(By.ID, "st")

soup = BeautifulSoup(driver.page_source, 'lxml')
table = soup.find('section', class_='col-center')
for listing in soup.find_all('li'):
    for items in listing:
        print(items.get_text())
#   for name in listing.find():
#       print(name)



#print(torrent_li)
#driver.quit()



