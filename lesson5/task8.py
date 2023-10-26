def getMaxNumberLength() -> int:
    currentLength = maxLength = previousNumber = 0
    currentNumber = int(input())
    while currentNumber != 0:
        if currentNumber == previousNumber:
            currentLength += 1
        else:
            previousNumber = currentNumber
            maxLength = max(currentLength, maxLength)
            currentLength = 1
        currentNumber = int(input())
    return max(currentLength, maxLength)

maxLength = getMaxNumberLength()
print(maxLength)