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


def print_company_position(cadena):
    """Function that returns the portion of string between the "#" and a blankspace"""
    for i in range(len(cadena)):
        if cadena[i] == "#":
            j = i
            while cadena[j] != " ":
                j = j+1
            return cadena[i:j] 


def print_company_name(cadena):
    """Function that returns the portion of string between quotes after the "|" """
    for i in range(len(cadena)):
        if cadena[i] == "|":
            while cadena[i] != '"':
                i = i+1
            else:
                j = i+1
                while cadena[j] != '"':
                  j = j +1
                return cadena[i+1:j]
      

# Main
req = requests.get(DATASET)
html = BeautifulSoup(req.text, 'html.parser')

contenido = html.find(class_='article-body')
contenido_empresas = contenido.find_all('h3')

for componente in contenido_empresas:
    #print(componente)
    componente = str(componente)
    company_rank = print_company_position(componente)
    company_name = print_company_name(componente)
    print(company_rank, end="")
    print(": ", end="")
    print(company_name)



