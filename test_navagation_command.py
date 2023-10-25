import time

from selenium import webdriver

browser = webdriver.Chrome()

# get()- acessa a página do google
browser.get("https://www.google.com")

# maximize_window() - maximiza o página
browser.maximize_window()
time.sleep(1)  # esperar 1s

# refresh() - F5
browser.refresh()

browser.get("https://www.saucedemo.com/")
time.sleep(1)  # esperar 1s

# back()
browser.back()
time.sleep(1)  # esperar 1s

# forward()
browser.forward()
time.sleep(1)  # esperar 2s

# cria/abre uma nova aba(guia)
# browser.switch_to.new_window("tab")
# time.sleep(3)  # esperar 2s
#
# # close() - fecha a guia atual
# browser.close()
# time.sleep(3)  # esperar 2s

# quit() - fecha todas as janelas de uma vez
browser.switch_to.new_window()
browser.switch_to.new_window()
time.sleep(1)
browser.quit()
time.sleep(1)
