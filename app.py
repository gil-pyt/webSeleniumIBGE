from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ibge = 'https://www.ibge.gov.br/en/indicators.html';

# Inicializa o WebDriver
driver = webdriver.Chrome()

# Abre o site desejado
driver.get(ibge)

# Espera a página carregar completamente
time.sleep(3)

# Pegar tabela
tabela = driver.find_element(By.CSS_SELECTOR, '.indicadores-tabela.economic-indicators')

print("Dados do IBGE:") 
print(tabela.text) 

# Fechar o navegador
driver.quit()

