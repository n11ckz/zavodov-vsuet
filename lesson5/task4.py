def calculateDay(x: int, y: int) -> None:
    day = 1
    while x < y:
        x *= 1.1
        day += 1
    print(day)

calculateDay(2, 9)