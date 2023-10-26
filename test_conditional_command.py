import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")
time.sleep(2)

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

#is_displayed() - retorna true se o elemento estiver visível
print("O campo username está visível?", username.is_displayed())
assert username.is_displayed()

#is_enabled() - retorna true se o elemento estiver habilidado
print("O campo usarname está habilitado?", username.is_enabled())
assert username.is_enabled()

#is_selected() - retorna true se o elemento estiver selecionado
print("O checkbox está selecionado?", checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

#clicando no checkbox
checkbox_remember_me.click()
print("O checkbox está selecionado?", checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()
