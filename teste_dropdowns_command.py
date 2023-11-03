import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

drowpdown_products = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
drowpdown_products.select_by_visible_text("Google")
time.sleep(3)

drowpdown_animals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
drowpdown_animals.select_by_value("babycat")
time.sleep(3)
drowpdown_animals.select_by_index(2)
time.sleep(3)

drowpdown_food = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
drowpdown_food.select_by_visible_text("Pizza")
time.sleep(2)
drowpdown_food.select_by_visible_text("Donut")
time.sleep(3)
