# вариант 2
def createUserArray(N: int) -> list:
    array: list = []
    for i in range(N):
        array.append(int(input()))
    return array

userArray: list = createUserArray(5)
print(userArray.index(min(userArray)))