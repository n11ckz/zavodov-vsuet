def getMinDivider(number: int) -> int:
    if number < 2:
        return 0
    for i in range(2, number + 1):
        if number % i == 0:
            return i

divider: int = getMinDivider(7)
print(divider)