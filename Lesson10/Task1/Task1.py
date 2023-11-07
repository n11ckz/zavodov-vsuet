# вариант 2
def convertFileToMatrix(path: str) -> list:
    return []

def isSquareMatrix(array: list) -> bool:
    lengthToCompare = len(array)
    for i in range(len(array)):
        if len(array[i]) != lengthToCompare:
            return False
    return True

def isMagicMatrix(array: list) -> bool:
    if not isSquareMatrix(array):
        return False
    sumToCompare = sum(array[0])
    rowSum, columnSum = 0, 0
    for i in range(len(array)):
        rowSum = sum(array[i])
        for j in range(len(array[i])):
            columnSum += array[j][i]
        if (rowSum != sumToCompare) or (columnSum != sumToCompare):
            return False
        rowSum, columnSum = 0, 0
    return True


path: str = "Input.txt"
fileLines = open(path).readlines()
matrix: list = []
for i in fileLines:
    tempArray: list = []
    for j in i.split():
        tempArray.append(int(j))
    matrix.append(tempArray)
print(matrix)