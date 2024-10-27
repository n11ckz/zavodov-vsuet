# вариант 2
def getMatrixFromFile(filePath: str) -> list:
    fileLines = open(filePath).readlines()
    fileMatrix: list = []
    for i in fileLines:
        tempArray: list = []
        for j in i.split():
            tempArray.append(int(j))
        fileMatrix.append(tempArray)
    return fileMatrix

def writeResultInFile(filePath: str, result: str) -> None:
    file = open(filePath, mode='w')
    file.write(result)
    file.close()

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

matrix: list = getMatrixFromFile("input.txt")
if isMagicMatrix(matrix):
    writeResultInFile("output.txt", "Матрица является магическим квадратом")
else:
    writeResultInFile("output.txt", "Матрица не является магическим квадратом")