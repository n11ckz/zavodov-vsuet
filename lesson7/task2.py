# вариант 2
def sortArrayBySign(array: list, isPositive: bool) -> []:
    sortedArray = []
    for i in range(len(array)):
        if array[i] >= 0 and isPositive:
            sortedArray.append(array[i])
        elif array[i] < 0 and not isPositive:
            sortedArray.append(array[i])
    return sortedArray


numbers = [-7, 6, 8, -1, 11, -3, 0, 15, 8]
positiveNumbers = sortArrayBySign(numbers, True)
negativeNumbers = sortArrayBySign(numbers, False)
print(f"{positiveNumbers}\n{negativeNumbers}")