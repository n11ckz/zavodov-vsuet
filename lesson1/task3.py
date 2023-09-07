def isEntered(age, name):
    if age < 7 or age > 75:
        return False
    if age >= 7 and age < 16:
        print(f"Сначала нужно окончить школу\nТебе осталось учиться {16 - age}")
        return False
    if name.lower() == "иван":
        return False
    return True

age = int(input())
name = input()
if isEntered(age, name):
    print("Поздравляем вы поступили в ВГУИТ")
    # последующая логика программы