def getMaxNumberLength() -> int:
    currentLength: int = 0
    maxLength: int = 0
    previousNumber: int = 0
    currentNumber: int = int(input())
    while currentNumber != 0:
        if currentNumber == previousNumber:
            currentLength += 1
        else:
            previousNumber = currentNumber
            maxLength = max(currentLength, maxLength)
            currentLength = 1
        currentNumber = int(input())
    return max(currentLength, maxLength)

maxLength: int = getMaxNumberLength()
print(maxLength)