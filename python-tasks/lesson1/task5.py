def calculateExpression(number: int) -> int:
    return number + number ** 2 + number ** 3 + number ** 4 + number ** 5

result: int = calculateExpression(5)
print(result)