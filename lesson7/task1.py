# вариант 2
def createUserArray(N: int) -> []:
    array = []
    for i in range(N):
        array.append(int(input()))
    return array

userArray = createUserArray(5)
print(userArray.index(min(userArray)))