import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1600,900")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver_ya = webdriver.Firefox()

driver_ya.get("https://google.com")
driver.get("https://ya.ru")
time.sleep(100)


driver.quit()