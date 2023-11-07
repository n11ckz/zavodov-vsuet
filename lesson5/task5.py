def calculateLength() -> int:
    numbers = []
    number = int(input())
    while number != 0:
        numbers.append(number)
        number = int(input())
    return len(numbers)

length: int = calculateLength()
print(length)