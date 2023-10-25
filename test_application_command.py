import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/") # acessa a página do saucedemo
time.sleep(2) # esperar 2s

#mostra o título da página
print("O título da página é:", browser.title)

#mostra a URL da página
print("A URL da página é:", browser.current_url)

#mostra o código-fonte da página
print("O código-fonte da página é:", browser.page_source)