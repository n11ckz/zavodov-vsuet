# вариант 2
def sortArrayBySign(array: list, isPositive: bool) -> list:
    sortedArray: list = []
    for i in range(len(array)):
        if array[i] >= 0 and isPositive:
            sortedArray.append(array[i])
        elif array[i] < 0 and not isPositive:
            sortedArray.append(array[i])
    return sortedArray


numbers: list = [-7, 6, 8, -1, 11, -3, 0, 15, 8]
positiveNumbers: list = sortArrayBySign(numbers, True)
negativeNumbers: list = sortArrayBySign(numbers, False)
print(f"{positiveNumbers}\n{negativeNumbers}")