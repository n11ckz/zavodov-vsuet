def getNumbersFromRange(a: int, b: int) -> []:
    if a > b:
        return
    return [*range(a, b + 1)]

numbers: list = getNumbersFromRange(5, 15)
print(numbers)