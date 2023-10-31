import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

#a cada comando, então eu devo esperar até 12 segundos, ou seja, no máximo 12s. Se antes dos 12s aparecer o que estou querendo, então ele vai seguir com o teste
browser.implicitly_wait(12)
browser.get("https://chercher.tech/practice/implicit-wait-example")

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()
time.sleep(3)
print('Checkbox está na tela!')


"""
Comandos de Espera(wait)
element.
time.sleep()
implicitly_wait()
explicitly_wait()
"""