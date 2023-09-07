import math

# уравнение №1
def calculateExpression(x, y, z):
    return ((2 * math.cos(x - (2 / 3))) / ((1 / 2) + (math.sin(y) ** 2))) * (1 + ((z ** 2) / (3 - ((z ** 2) / 5))))

x = 14.26
y = -1.22
z = 3.5 * 10 ** -2
print(calculateExpression(x, y, z))