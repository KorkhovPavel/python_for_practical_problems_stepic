# Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью,
# у него сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить зарплатную
# ведомость. Архив с расчётными листками доступен по ссылке
# https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
# (вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).
#
# Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел,
# его зарплата. Сотрудники должны быть упорядочены по алфавиту.

import zipfile
import urllib.request

import xlrd

urllib.request.urlretrieve('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip', 'rogaikopyta.zip')
fantasy_zip = zipfile.ZipFile('rogaikopyta.zip')
fantasy_zip.extractall('rogaikopyta')
fantasy_zip.close()

d = []
for i in range(1, 1001):
    rb = xlrd.open_workbook(f'rogaikopyta/{i}.xlsx')
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    d.append(f'{vals[1][1]} {int(vals[1][3])}\n')
d = sorted(d)

# for i in d:
#     print(i)
with open('text.txt', 'w', encoding='utf-8') as txt_file:
    for i in d:
        txt_file.write(i)
