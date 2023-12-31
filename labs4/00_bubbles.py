#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(600,350)
radius = 50
for _ in range(3):
    sd.circle(center_position=point, radius=radius)
    radius += 5

# Написать функцию рисования пузырька, принимающую 3 (или более) параметра: точка рисования, шаг и цвет
def draw_babble(point, step, color, cnt_bubbles):
    radius = 50
    for _ in range(cnt_bubbles):
        sd.circle(center_position=point, radius=radius, color=color)
        radius += step

draw_babble(point=sd.get_point(300,300),step=10,color=[255,0,0], cnt_bubbles=10)

# Нарисовать 10 пузырьков в ряд
for x in range(100,1100,100):
    draw_babble(point=sd.get_point(x, 100), step=0, cnt_bubbles=1, color=[255,0,0])


# Нарисовать три ряда по 10 пузырьков
for y in range(100,500,150):
    for x in range(100,1100,100):
        draw_babble(point=sd.get_point(x, y), step=0, cnt_bubbles=1, color=[255,0,0])


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    draw_babble(sd.random_point(), step=0, cnt_bubbles=1, color=sd.random_color())

sd.pause()