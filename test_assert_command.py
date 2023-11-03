# o assert sempre verifica se o retorno da condição é True

#assert True
#assert False

#assert numbers
# num_esperado = 2
# num_obtido = 1
# assert num_esperado == num_obtido, f"Esperado {num_esperado}. Atual {num_obtido}"

#assert text
# text_esperado = "Selenium Webdriver"
# text_obtido = "Selenium webdriver"
# assert text_esperado.lower() == text_obtido.lower(), f"O texto Esperado seria: {text_esperado} e o texto Atual foi: {text_obtido}"

#assert text in string
text_esperado = "Seleniumzzzzzzz"
text_obtido = "Selenium Webdriver"
#assert text_esperado in text_obtido, f"O texto Esperado '{text_esperado}' 'está dentro da strig Atual '{text_obtido}'"
assert text_esperado not in text_obtido, f"O texto Esperado '{text_esperado}' 'está dentro da strig Atual '{text_obtido}'"

#assert is_displayed / is_enabled / is_selected
