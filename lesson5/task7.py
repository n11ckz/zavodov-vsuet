def calculatePrevious() -> int:
    previous = int(input())
    count = 0
    while previous != 0:
        next = int(input())
        if next != 0 and previous < next:
            count += 1
        previous = next
    return count

count = calculatePrevious()
print(count)