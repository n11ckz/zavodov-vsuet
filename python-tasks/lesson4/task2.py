def getNumbersFromRange(a: int, b: int) -> list:
    if a <= b:
        return [*range(a, b + 1)]
    else:
        return [*range(a, b - 1, -1)]

numbers: list = getNumbersFromRange(20, 15)
print(numbers)