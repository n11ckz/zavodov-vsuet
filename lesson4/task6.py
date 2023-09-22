def calculateFactorial(n) -> int:
    if n <= 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = calculateFactorial(5)
print(number)