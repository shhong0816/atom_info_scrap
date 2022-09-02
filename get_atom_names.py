import csv

row_num = 0

with open("get_atoms_data.csv","r", encoding = 'utf8') as target_file:
    csv_data = csv.reader(target_file)
    print(csv_data)
    for row in csv_data:
        if row_num == 2:
            atom_names = row
        row_num += 1
## 원소 이름들 추출 리스트 -> atom_names

with open("atom_names.csv","w", encoding = 'utf-8', newline="") as want_file:
    write = csv.writer(want_file, delimiter = '\n', quotechar = ',', quoting = csv.QUOTE_ALL)
    write.writerow(atom_names)

print(atom_names)
