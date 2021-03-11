# В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица. Просуммируйте все числа
# в ней
# и введите в качестве ответа одно число - эту сумму. Для доступа к ячейкам используйте возможности BeautifulSoup.

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html').read().decode('utf-8')
print(html)
print('-------------------')
soup = BeautifulSoup(str(html), 'html.parser')
res = 0
for i in soup.find_all('td'):
    num = i.text
    num_1 = int(num[1:5])
    res += num_1

print(res)
