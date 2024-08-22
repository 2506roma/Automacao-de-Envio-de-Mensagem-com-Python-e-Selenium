from certifi import where
from selenium import webdriver
import time
import urllib
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#Lê os documentos em excel
import openpyxl
from AutoEscala.Anaconda.anateste import navegador

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# Esperar o whatsapp carregar abrindir o QRcode
while len(navegador.find_elements(By.ID,'side')) < 1:  # <- Enquanto o tamanho da lista for menor que um == loop se for maior == proximo
    time.sleep(1)  # enquanto a lista não carregar sera adicionado 1 segundo
time.sleep(2)  # Garantia
#Whatsapp carregado
#Guardando a base de dados
tabela = pd.read_excel(r"C:\Users\PESSOAL\Desktop\AutoEscala\BaseDadosCel.xlsx")

#Laço para carregar a base de dados
for linha in tabela.index:

    #Variavel linha vai percorrer todos os dados e guardar na lista
    nome = tabela.loc[linha, "Nome"]
    mensagem = tabela.loc[linha, "Mensagem"]
    arquivo = tabela.loc[linha, "Arquivo"]
    numero = tabela.loc[linha,"Telefone"]

    #Substitur os nomes
    texto = mensagem.replace("fulano", nome)
    #Formatando o texto para entrar no link
    texto = urllib.parse.quote(texto)

    #Enviar mensagem para o contato
    link = f"https://web.whatsapp.com/send?phone=+{numero}&text={texto}"
    navegador.get(link)

    #Esperar o whatsapp carregar -> esperar um elemento especifico da tela
    time.sleep(1)
    #Elementos verifica se a pagina carregou
    while len(navegador.find_elements(By.ID, 'side')) < 1: # <- Enquanto o tamanho da lista for menor que um == loop se for maior == proximo
        time.sleep(1)#enquanto a lista não carregar sera adicionado 1 segundo
    time.sleep(5)#Garantia
    #Enviar a mensagem
    #input("Pressione Enter para continuar...")
    navegador.find_element(By.XPATH, '    // *[ @ id = "main"] / footer / div[1] / div / span[2] / div / div[2] / div[2] / button / span').click()
    time.sleep(3)

