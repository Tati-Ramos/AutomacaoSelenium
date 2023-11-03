import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/") # acessa a página do saucedemo
time.sleep(2) # esperar 2s

#find_element() - encontra um elemento
usarname = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login =browser.find_element(By.ID, "login-button")

#send_keys()
usarname.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(2)

#click() - realizando o login
btn_login.click()

#text - na area logada
products_title = browser.find_element(By.XPATH, "//span[@class='title']")
print(products_title.text)
assert products_title.text == "Products"

#get_attribute()

img_backpack = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(img_backpack.get_attribute("alt"))
assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack"
#assert img_backpack.is_displayed() - se está aparecendo
assert not img_backpack.is_displayed() # se não estiver aparecendo

time.sleep(1)
browser.quit()
