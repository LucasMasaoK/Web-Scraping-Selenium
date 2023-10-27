import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.ChromiumEdge()
driver.get("https://www.novaliderinformatica.com.br/computadores")
time.sleep(3)
titulos = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")
precos =  driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")
produtos=[]
precosArray=[]
for titulo in titulos:
    produtos.append(titulo.text)

for preco in precos:
    precosArray.append(preco.text)

for i in range(1,len(precosArray)):
    print(produtos[i]+'\n'+precosArray[i])


