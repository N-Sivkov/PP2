import math


#1
a = math.radians(float(input()))
print(a)
print()

#2
h, b1, b2 = float(input()), float(input()), float(input())
area = (b1 + b2) / 2 * h
print(area)
print()

#3
n, lenSide = int(input()), float(input())
angle = math.radians(180 / n)
apothem = (lenSide / (2 * math.tan(angle)))
area = (n * lenSide * apothem) / 2
print(area)

#4
b, h = float(input()), float(input())
area = b * h
print(area)