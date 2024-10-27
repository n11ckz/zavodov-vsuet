def getAllOddNumbers(a: int, b: int) -> list:
    if a <= b:
        return []
    oddNumbers: list = []
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            oddNumbers.append(i)
    return oddNumbers

numbers: list = getAllOddNumbers(20, 10)
print(numbers)