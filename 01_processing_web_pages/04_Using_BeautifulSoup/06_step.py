# В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица. Просуммируйте
# все числа в ней. Теперь мы не только добавили разных тегов для изменения стиля отображения, но и
# сделали невалидный HTML-код (правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы).
# Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.
#
# Вы можете исправить html-код или попробовать использовать нестандартный парсер html, такой как html5lib.

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html').read().decode('utf-8')
soup = BeautifulSoup(str(html), 'html.parser')
print(soup)
res = 0
for i in soup.find_all('td'):
    num = i.text
    print(num)
    num_1 = int(num[1:5])
    res += num_1
print(res)