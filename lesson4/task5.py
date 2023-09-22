def calculateExpression(n) -> int:
    if n <= 0:
        return 0
    result = 0
    for i in range(n + 1):
        result += i ** 3
    return result

number = calculateExpression(4)
print(number)