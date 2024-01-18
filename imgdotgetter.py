s = "69% 12%, 70% 15%, 73% 15%, 74% 23%, 77% 23%, 76% 29%, 81% 32%, 81% 37%, 77% 40%, 64% 43%, 45% 39%, 44% 40%, 43% 35%, 41% 38%, 40% 32%, 21% 5%);"
nums = s.replace("%", "").split(", ")
print(nums)
for num in nums:    
    n = num.split(" ")
    print(int(n[1])*1.7333333)
raise

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