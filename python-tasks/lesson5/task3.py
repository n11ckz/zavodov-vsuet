def showPowerOfNumber(number: int) -> None:
    count: int = 0
    power: int = 1
    while power * 2 < number:
        count += 1
        power *= 2
    print(count, power)

showPowerOfNumber(32)