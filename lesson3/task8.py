def matchCount(array: list) -> int:
    array = sorted(array)
    count: int = 0
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            count += 1
    if count == 0:
        return 0
    return count + 1

numbers: list = [5, -1, -1]
print(matchCount(numbers))