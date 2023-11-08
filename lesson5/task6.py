def calculateAverageValue() -> float:
    numbers: list = []
    number: int = int(input())
    while number != 0:
        numbers.append(number)
        number = int(input())
    return sum(numbers) / len(numbers)

averageValue: float = calculateAverageValue()
print(averageValue)