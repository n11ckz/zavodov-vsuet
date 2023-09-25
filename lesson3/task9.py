def canBreak(N, M, K) -> bool:
    return ((K % N == 0) or (K % M == 0)) and (K < N * M)

if canBreak(2, 3, 2):
    print("Yep")
else:
    print("No")