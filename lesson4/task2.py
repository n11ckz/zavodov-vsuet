def getNumbersFromRange(a: int, b: int) -> []:
    if a <= b:
        return [*range(a, b + 1)]
    else:
        return [*range(a, b - 1, -1)]

numbers = getNumbersFromRange(20, 15)
print(numbers)