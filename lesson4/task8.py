def printSteps(n: int) -> None:
    if 9 < n >= 0:
        return
    step = ""
    for i in range(1, n + 1):
        step += f"{i}"
        print(step)

stepsCount = 9
printSteps(stepsCount)