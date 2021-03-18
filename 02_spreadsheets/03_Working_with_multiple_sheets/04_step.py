# Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник
# продуктов с указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм
# продукта. Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными
# (можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял
# целую и дробную часть чисел запятой. Таблица доступна по ссылке
# https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx
#
# Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера
# дня, названия продукта и его количества в граммах. Для каждого дня посчитайте 4 числа: суммарную калорийность
# и граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел. Информация о каждом
# дне должна выводиться в отдельной строке.

import math

import xlrd

rb = xlrd.open_workbook('trekking3.xlsx')

sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

sheet_1 = rb.sheet_by_index(1)
vals_1 = [sheet_1.row_values(rownum) for rownum in range(sheet_1.nrows)]

count = 0
lst = [0, 0, 0, 0]
d = {}
for i in vals_1[1:]:
    if count != i[0]:
        if count != 0:
            print(f'день {int(count)}   ', math.floor(lst[0]), math.floor(lst[1]), math.floor(lst[2]),
                  math.floor(lst[3]))
        lst = [0, 0, 0, 0]
    count = i[0]
    for v in vals[1:]:
        if i[1] == v[0]:
            lst[0] += (v[1] / 100) * i[2]
            lst[1] += (v[2] / 100) * i[2]
            lst[2] += (v[3] / 100) * i[2]
            lst[3] += (v[4] / 100) * i[2]

print(f'день {int(count)}   ', math.floor(lst[0]), math.floor(lst[1]), math.floor(lst[2]), math.floor(lst[3]))
