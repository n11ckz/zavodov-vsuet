# вариант 2
def showMatrix(array: list) -> None:
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end="\t")
        print()
    print()

def swapFirstAndLastColumns(array: list) -> None:
    for i in range(len(array)):
        array[i][0], array[i][-1] = array[i][-1], array[i][0]

matrix = [[5, 7, 3, 0],
          [9, 5, 1, 2],
          [7, 3, 8, 1]]
showMatrix(matrix)
swapFirstAndLastColumns(matrix)
showMatrix(matrix)