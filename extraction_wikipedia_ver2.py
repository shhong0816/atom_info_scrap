import csv
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re


row_num = 0
atoms = []
with open("atom_names.csv","r", encoding = 'utf8') as target_file:
    csv_data = csv.reader(target_file)
    for row in csv_data:
        if row_num < 2:
            row_num += 1
        elif row_num >= 2 and row_num <7:###97:
            row_num += 1
            atom = row[0]
            atoms.append(atom)  ##atoms에 list화 됨

URL = 'https://en.wikipedia.org/wiki/'
response = requests.get(URL+"oxygen")
soup = BeautifulSoup(response.text, "lxml"###html 추출완료

get_data = soup.find_all("span",attrs={"class":"nowrap"})
for i in get_data:
    k = i.find("span",attrs={"data-sort-value":re.compile("[0-9]{0,25}.")})
