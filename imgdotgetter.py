import pygame
import math

img = pygame.image.load("dots.png")

hight = img.get_height()
width = img.get_width()

midpoint = (width/2, hight/2)

pointList = []
for y in range(hight):
    for x in range(width):
        color = img.get_at((x, y))
        if color != (255, 255, 255, 255):
            pointList.append((int(100*x/width), int(100*y/hight), color[0]))

pointList.sort(key=lambda x: math.atan2((x[1] - 50), (x[0] - 50)))
pointList.sort(key=lambda x: x[2])

for point in pointList:
    print(point[0], "% ", point[1], "%, ", sep="", end="")