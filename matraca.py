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

################################################
# URL = sys.argv[1]
#URL = "https://www.linkedin.com/jobs/meli%C3%A1-hotels-international-jobs-worldwide?f_C=10838&trk=job-results_see-all-jobs-link&position=1&pageNum=0"
#string1 = ""

#req = requests.get(URL)
#html = BeautifulSoup(req.text, 'html.parser')

#print(html.title)
#print(len(html.title.contents))
#string1 = str(html.title)
#print(string1)
#print(len(string1))
#print(string1[7:10])
#print("")
###############################################
