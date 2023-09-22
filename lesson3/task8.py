def matchCount(array) -> int:
    array = sorted(array)
    count = 0
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            count += 1
    if count == 0:
        return 0
    return count + 1

numbers = [5, -1, -1]
print(matchCount(numbers))