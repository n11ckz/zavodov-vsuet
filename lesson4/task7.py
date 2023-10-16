def calculateExpression(n: int) -> int:
    if n <= 0:
        return 0
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(i * factorials[i - 1])
    return sum(factorials) - 1

number = calculateExpression(5)
print(number)