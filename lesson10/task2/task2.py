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

def writeResultInFile(filePath: str, array: list) -> None:
    file = open(filePath, mode='w')
    for i in range(len(array)):
        for j in range(len(array[i])):
            file.write(f"{array[i][j]}\t")
        if i != len(array) - 1:
            file.write("\n")
    file.close()

def swapFirstAndLastColumns(array: list) -> None:
    for i in range(len(array)):
        array[i][0], array[i][-1] = array[i][-1], array[i][0]

matrix: list = getMatrixFromFile("input.txt")
swapFirstAndLastColumns(matrix)
writeResultInFile("output.txt", matrix)