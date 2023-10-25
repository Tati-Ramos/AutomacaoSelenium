import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.google.com") # acessa a página do google
time.sleep(5) # esperar 5s
