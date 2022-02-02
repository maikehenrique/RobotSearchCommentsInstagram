from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
from os.path import basename
import json
import os
import time
from datetime import datetime
import urllib.request
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class InstagramBot:

    links = []

    def __init__(self):
        print('Iniciando Projeto')

    def busca(self):

        self.telainicial()
        print("Digite os links a serem buscados: ")
        print('URL    |   Comentários')
        while 1:
            try:
                url = input()
                req = Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                                            "X-Requested-With": "XMLHttpRequest"})
                pagina = urlopen(req).read()
                htmlpagina = BeautifulSoup(pagina, 'html.parser')
                titulo = htmlpagina
                type(htmlpagina)
                htmlpagina = htmlpagina.find(
                    'meta', property="og:description").attrs['content']

                qtdcomentarios = htmlpagina[9: 24].split(' ')[1]
                qtdcomentarios = qtdcomentarios.replace(",", ".")
                titulo = str(titulo.find('title').text)

                print(titulo[0:10] + " "+url+"       " +
                      str(qtdcomentarios) + " Comentários")
            except Exception as e:
                print(e)

    def telainicial(self):
        print("------------------------------------------------------------------------")
        print("                           Bot busca Comentaarios                 ")
        print("                                                                        ")
        print("Iniciando processo de Abrindo Site ...............                       ")
        print("")
        print(
            "----------------------------------------------------------------------------")
bot = InstagramBot()
bot.busca()
