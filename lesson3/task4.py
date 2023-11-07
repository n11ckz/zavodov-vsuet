def calculateLength(A: int, B: int, L: int, N: int) -> float:
    return 2 * L + (2 * N - 1) * A + 2 * (N - 1) * B

length: float = calculateLength(2, 5, 5, 10)
print(f"{length}мм")