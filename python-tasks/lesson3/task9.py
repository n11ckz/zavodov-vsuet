def canBreak(N: int, M: int, K: int) -> bool:
    return ((K % N == 0) or (K % M == 0)) and (K < N * M)

if canBreak(2, 3, 2):
    print("Да")
else:
    print("Нет")