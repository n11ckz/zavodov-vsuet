def calculateAverageValue() -> float:
    numbers = []
    number = int(input())
    while number != 0:
        numbers.append(number)
        number = int(input())
    return sum(numbers) / len(numbers)

averageValue = calculateAverageValue()
print(averageValue)