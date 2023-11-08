# вариант 2
def showMatrix(array: list) -> None:
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end="\t")
        print()

def isSquareMatrix(array: list) -> bool:
    lengthToCompare: int = len(array)
    for i in range(len(array)):
        if len(array[i]) != lengthToCompare:
            return False
    return True

def isMagicMatrix(array: list) -> bool:
    if not isSquareMatrix(array):
        return False
    sumToCompare: int = sum(array[0])
    columnSum: int = 0
    for i in range(len(array)):
        rowSum: int = sum(array[i])
        for j in range(len(array[i])):
            columnSum += array[j][i]
        if (rowSum != sumToCompare) or (columnSum != sumToCompare):
            return False
        columnSum = 0
    return True

matrix: list = [[2, 7, 6],
                [9, 5, 1],
                [4, 3, 8]]
showMatrix(matrix)
if isMagicMatrix(matrix):
    print(f"Матрица является магическим квадратом")
else:
    print(f"Матрица не является магическим квадратом")