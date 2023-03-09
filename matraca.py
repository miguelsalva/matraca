#!/usr/bin/env python3
#
# FILE: matraca.py
# AUTHOR: Miguel Salvá
# LICENSE: MIT License. Copyright (c) 2023 Miguel Salvá
# ABSTRACT: PoC for getting job vacancies from Linkedin company websites
#           Not to be run - only for educational purposes
#
# This script requires the beautifulsoup4 and requests libraries to run


import sys
import requests 
from bs4 import BeautifulSoup


DATASET = "https://www.forbes.com/sites/forbesstaff/2022/05/12/forbes-global-2000-list-2022-the-top-200/"


def print_position(cadena):
    for i in range(len(cadena)):
      if cadena[i] == "#":
          j = i
          while cadena[j] != " ":
              j = j+1
          return cadena[i:j] 
        

req = requests.get(DATASET)
html = BeautifulSoup(req.text, 'html.parser')

contenido = html.find(class_='article-body')
contenido_empresas = contenido.find_all('h3')

for componente in contenido_empresas:
    componente = str(componente)
    print(componente)
    num = print_position(componente)
    print(num)
    print("")
