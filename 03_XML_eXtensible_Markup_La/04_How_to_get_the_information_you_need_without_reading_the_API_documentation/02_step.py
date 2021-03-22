# Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой. Вася предполагает,
# что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре. Определите,
# сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты
# https://stepik.org/media/attachments/lesson/245681/map2.osm


from bs4 import BeautifulSoup

fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
counter = 0
for v in ['way', 'node']:
    soup = BeautifulSoup(xml, 'lxml').find_all(f'{v}')
    s = BeautifulSoup(str(soup), 'lxml').find_all('tag', k='amenity', v='fuel')

    for i in s:
        # print(counter, i)
        counter += 1

print(counter)
