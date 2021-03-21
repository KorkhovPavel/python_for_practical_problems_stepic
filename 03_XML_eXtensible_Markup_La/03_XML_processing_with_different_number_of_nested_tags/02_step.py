# Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в
# интересующем его районе. Вася скачал интересующий его кусок карты OSM
# https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать,
# сколько на нём отмечено точечных объектов (node), являющихся заправкой.
# В качестве ответа вам необходимо вывести одно число - количество АЗС.
#
# "Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать,
# как обозначается заправка в OpenStreetMap

from bs4 import BeautifulSoup

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

soup = BeautifulSoup(xml, 'lxml').find_all('node')
s = BeautifulSoup(str(soup), 'lxml').find_all('tag', k='amenity', v='fuel')
counter = 1
for i in s:
    print(counter, i)
    counter += 1
