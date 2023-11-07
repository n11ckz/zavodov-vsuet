def calculatePrevious() -> int:
    previousNumber = int(input())
    count = 0
    while previousNumber != 0:
        nextNumber = int(input())
        if nextNumber != 0 and previousNumber < nextNumber:
            count += 1
        previousNumber = nextNumber
    return count

count: int = calculatePrevious()
print(count)