def createUserArray(n) -> []:
    array = []
    for i in range(n):
        array.append(int(input()))
    return array

userArray = createUserArray(int(input()))
print(userArray)