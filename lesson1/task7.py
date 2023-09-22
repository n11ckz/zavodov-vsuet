def isNumberEven(n) -> bool:
    if n % 2 != 0:
        return False
    return True

number = 16
if isNumberEven(number):
    print(f"{number} - четное число")
    # последующая логика программы