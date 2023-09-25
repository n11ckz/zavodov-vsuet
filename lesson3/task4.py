def calculateLength(A, B, L, N) -> float:
    return 2 * L + (2 * N - 1) * A + 2 * (N - 1) * B

length = calculateLength(2, 5, 5, 10)
print(f"{length}mm")