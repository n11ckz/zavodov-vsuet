import math

# уравнение №5
def calculateExpression(x: float, y: float, z: float) -> float:
    return (math.log(y ** (-math.sqrt(abs(x))), math.e) * (x - (y / 2))) + (math.sin(math.atan(z)) ** 2)

x: float = -15.246
y: float = 4.642 * 10 ** -2
z: float = 21
print(calculateExpression(x, y, z))