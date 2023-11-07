def calculateFibonacci(n: int) -> int:
    if n <= 1:
        return 0
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    print(fibonacci)
    return sum(fibonacci)

result: int = calculateFibonacci(15)
print(result)