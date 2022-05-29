from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
i = "test"
driver.get(f"https://thepiratebay.org/search.php?q={i}")



