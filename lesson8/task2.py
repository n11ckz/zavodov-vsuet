# вариант 2
def calculateAreaOfRectangle(a: float, b: float) -> float:
    return a * b

firstRectangle = calculateAreaOfRectangle(float(input()), float(input()))
secondRectangle = calculateAreaOfRectangle(float(input()), float(input()))
thirdRectangle = calculateAreaOfRectangle(float(input()), float(input()))
print(f"{firstRectangle}, {secondRectangle}, {thirdRectangle}")