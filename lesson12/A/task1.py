# задание 1
def calculateFactorial(number: int) -> int:
    if number == 0:
        return 1
    return calculateFactorial(number - 1) * number

def calculateExpression(x: int, n: int) -> float:
    return x ** n / calculateFactorial(n)

value: int = calculateExpression(3, 5)
print(value)