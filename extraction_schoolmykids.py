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

import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time

browser = webdriver.Chrome()
browser.get("https://www.schoolmykids.com/learn/interactive-periodic-table/young-modulus-of-all-the-elements")
time.sleep(1)
element = browser.find_element_by_tag_name('body')
element.send_keys(Keys.END)


#atom 이름 get
browse_atom = browser.find_element_by_class_name("table").find_element_by_tag_name("tbody").find_elements_by_class_name("hidden-xs")
atom_name = []
atoms = []
for e in browse_atom:
    atom_name.append(e.text)
atoms = atom_name[1::3]

##data get
data = []
num_check = []
num = 1
for d in range(99):#99
    browse_data = browser.find_element_by_xpath("/html/body/div[4]/div/div[1]/div[1]/div[3]/div[2]/div[2]/table/tbody/tr[{}]/td[5]".format(num))
    num_check.append(num)
    num += 1
    ##선택 1개
    # data.append(browse_data.text)
    a = Erase_num(browse_data.text,3)###################################################
    data.append(a)
    #
    # 

with open("get_atoms_data.csv","w", encoding = 'cp949',newline = "") as want_file:
    write = csv.writer(want_file)
    write.writerow(num_check)
    write.writerow(atoms)
    write.writerow(data)

browser.quit()
print("End")
