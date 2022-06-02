import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_interval
from openpyxl.utils import get_column_letter

first_file = "Лист1.xlsx"
second_file = "Лист2.xlsx"
third_file = "Лист3.xlsx"
first_file_list_global = []
second_file_list_global = []
third_file_list_global = []
files = [[first_file, first_file_list_global], [second_file, second_file_list_global],
         [third_file, third_file_list_global]]
# загружаем в память уже существующий файл на диске
# workbook1 = openpyxl.load_workbook(file_name)
#
# worksheet1 = workbook1.active
glob_list = []

for i in files:
    workbook = openpyxl.load_workbook(i[0])
    worksheet = workbook.active
    for y in range(1, 26):
        mass_local = []
        for x in range(1, 26):
            value = worksheet.cell(row=x, column=y).value
            if value is None:
                break
            mass_local.append(value)
        glob_list.append(mass_local)


    # filter(None, i[1])
    # i[1] = [x for x in i[1] if x]

    def iii():
        for ii in glob_list:
            # print("ii" + str(ii[0]))
            if len(ii) == 0:
                # print("ii")
                del glob_list[0]
                iii()

workbook2 = Workbook()
worksheet2 = workbook2.active

# row = 0
# col = 1
# for i in glob_list:
#     row += 1
#     for ii in i:
#         print(ii)
#         worksheet2.cell(row=row, column=col).value = str(ii)
#         print(type(worksheet2[f'{col}{row}'][0]))
#         col += 1
#     col = 1
#
# workbook2.save("sample_example.xlsx")
# iii()
# print(i[1])
print(glob_list)
row = 0
col = 1
coll = 1
for el in glob_list:

    print("el" + str(el))
    col = get_column_letter(coll)
    print(col)
    if len(el) == 0:
        coll -= 1
    for le in el:
        row += 1
        worksheet2[f'{col}{row}'] = str(le)
        print(le)
    coll += 1
    row = 0

workbook2.save("task1.xlsx")
