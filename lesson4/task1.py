def getNumbersFromRange(a, b) -> []:
    if a > b:
        return
    return [*range(a, b + 1)]

numbers = getNumbersFromRange(5, 15)
print(numbers)