#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

for city in sites.keys():
    for other in sites.keys():
        if city != other:
            x1, y1 = sites[city][0], sites[city][1]
            x2, y2 = sites[other][0], sites[other][1]
            if city + '-' + other not in distances and other + '-' + city not in distances:
                distances[city + '-' + other] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(distances)




