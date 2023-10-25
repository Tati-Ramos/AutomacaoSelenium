import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/") # acessa a página do saucedemo
time.sleep(2) # esperar 2s

#find_element() - encontra um elemento
# usarname = browser.find_element(By.ID, "user-name")
# password = browser.find_element(By.ID, "password")

#send_keys - escreve os textos nos campos usarname e password
# usarname.send_keys("standard_user")
# password.send_keys("secret_sauce")

#find_elements() - encontra mais de um elemento
auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")
print(auth_fields)
print(len(auth_fields))

#verificar pré-condições e condições esperadas durante a execução de um programa
assert len(auth_fields) == 3, "O número de elementos encontrados é diferente do esperado."

time.sleep(2)
browser.quit()



