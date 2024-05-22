from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('http://www.google.com')

elem = driver.find_element(By.NAME, 'p')  # Find the search box
#celem.send_keys('seleniumhq' + Keys.RETURN)

driver.quit()

