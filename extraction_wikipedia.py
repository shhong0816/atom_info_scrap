import csv
import re
import urllib.request

row_num = 0
atoms = []

##원소 영어이름 뽑아 list화
with open("atom_names.csv","r", encoding = 'utf8') as target_file:
    csv_data = csv.reader(target_file)
    for row in csv_data:
        if row_num < 2:
            row_num += 1
        elif row_num >= 2 and row_num <97:
            row_num += 1
            atom = row[0]
            atoms.append(atom)  ##atoms에 list화 됨
base_url = "https://en.wikipedia.org/wiki/"
make_list = []
atom_num = 0
for atom in atoms:
    atoms_url = base_url + atom
    atoms_html = urllib.request.urlopen(atoms_url)
    atoms_html_contents = str(atoms_html.read())
    get_result = re.findall(r"(Heat of vaporizatio.{1,100}infobox-data.>[0-9^&]{0,7}[\.–0-9^&][0-9^&]{0,7}&.{0,10}kJ/mol)",atoms_html_contents)
    atom_num += 1##진행정도 check
    print(get_result,atom,atom_num)
    if get_result == []:##추출실패로 인한 에러방지
         make_list.append("0")
         continue
    get_result_str = str(get_result[0])
    #get_result_letter = get_result_str.split(",")
    #get_letter = get_result_letter[0]
    count_ = 0
    letter = []
    get_inverse_letter = []
    for char in get_result_str:## 글자 하나하나 리스트 넣기
        letter.append(char)
    letter_inverse = letter[::-1]##글자 거꾸로 써서 뒤에 숫자 뽑아내기위해
    for main_char in letter_inverse:##숫자까지 뽑아내기
        if main_char == ">" or main_char == " ":
            break
        else:
            get_inverse_letter.append(main_char)
    letter_reinverse = get_inverse_letter[:11:-1]## letter_inverse -> 드디어 숫자만 뽑아냄
    get_val_str = ''.join(letter_reinverse)
    print(atom,get_val_str)
    make_list.append(get_val_str)

with open("get_atoms_data.csv","w", encoding = 'utf-8') as want_file:
    write = csv.writer(want_file)
    write.writerow(atoms)
    write.writerow(make_list)
