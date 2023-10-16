def getNumbersFromRange(a: int, b: int) -> []:
    if a > b:
        return
    return [*range(a, b + 1)]

numbers = getNumbersFromRange(5, 15)
print(numbers)