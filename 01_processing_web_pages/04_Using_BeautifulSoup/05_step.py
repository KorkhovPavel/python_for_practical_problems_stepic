# В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица. Просуммируйте
# все числа в ней. Теперь мы добавили разных тегов для изменения стиля отображения. Для доступа к ячейкам
# используйте возможности BeautifulSoup.
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html').read().decode('utf-8')
soup = BeautifulSoup(str(html), 'html.parser')
print(soup)
res = 0
for i in soup.find_all('td'):
    num = i.text
    print(num)
    num_1 = int(num[1:5])
    res += num_1
print(res)