def calculateFibonacci(n: int, k: int) -> int:
    if n <= 1 or k <= 0 or k > n:
        return 0
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    fibonacci = fibonacci[k - 1:]
    print(fibonacci)
    return sum(fibonacci)

result = calculateFibonacci(10, 3)
print(result)