# вариант 2
def calculateAreaOfRectangle(a: float, b: float) -> float:
    return a * b

firstRectangle: float = calculateAreaOfRectangle(float(input()), float(input()))
secondRectangle: float = calculateAreaOfRectangle(float(input()), float(input()))
thirdRectangle: float = calculateAreaOfRectangle(float(input()), float(input()))
print(f"{firstRectangle}, {secondRectangle}, {thirdRectangle}")