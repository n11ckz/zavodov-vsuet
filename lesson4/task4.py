def createUserArray(n: int) -> []:
    array = []
    for i in range(n):
        array.append(int(input()))
    return array

userArray = createUserArray(int(input()))
print(userArray)