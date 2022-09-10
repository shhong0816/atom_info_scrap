##tryyy


def Erase_num(target,e_num):
    l = []
    for i in target:###get list
        l.append(i)
    re_l = l[::-1]
    end_num = len(l)
    re_l_get_need = re_l[e_num:end_num]
    rere_l = re_l_get_need[::-1]
    str_rere_l = ''.join(rere_l)
    return(str_rere_l)

def get_unit(target,e_num):
    l = []
    for i in target:###get list
        l.append(i)
    re_l = l[::-1]
    end_num = len(l)
    re_l_get_need = re_l[e_num-10:end_num]
    rere_l = re_l_get_need[::-1]
    str_rere_l = ''.join(rere_l)
    return(str_rere_l)


import csv
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time


data = []
number =[]
check = []
unit_in = []
tit_check = []
browser = webdriver.Chrome()
for num in range(1,98):##98
    try:
        browser.get("https://pubchem.ncbi.nlm.nih.gov/element/" + str(num))
        time.sleep(1)
        title = browser.find_element_by_xpath("//*[@id='Boiling-Point']/div[1]/div/h3/span[2]")
        want = browser.find_element_by_xpath("//*[@id='Boiling-Point']/div[2]/div[1]/p")
        source = browser.find_element_by_xpath("//*[@id='Boiling-Point']/div[2]/div[2]/div/button/span")



        tit_check.append(title.text)

    ###표에 넣을 완벽한 수 , 둘중 하나방식선택
        a = Erase_num(want.text,21)
        data.append(a)
        # data.append(want.text)

    ###단위가 want에 있b을때
        b = get_unit(want.text,21)
        unit_in.append(b)



        number.append(num)
        check.append(source.text)
        print(want.text,num)
    except:
        data.append("Non")
        unit_in.append("Non")
        number.append(num)
        check.append("Non")
        print(num,"번에 오류있습니")
        continue


with open("get_atoms_data.csv","w", encoding = 'utf-8',newline = "") as want_file:
    write = csv.writer(want_file)
    write.writerow(number)
    write.writerow(tit_check)
    write.writerow(data)
    write.writerow(unit_in)
    write.writerow(check)

print("Fin")
