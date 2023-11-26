# задание 2
def getSecondMax(array: list) -> int:
    if array[-1] != 0:
        array.append(0)
    array.remove(max(array))
    return max(array)

numbers = [1, 5, 7, 8, 23, 67, 12, -1, 0]
secondMax = getSecondMax(numbers)
print(secondMax)