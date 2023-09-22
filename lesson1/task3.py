def isEntered(age, name) -> bool:
    if age < 7 or age > 75:
        return False
    if 7 <= age < 16:
        print(f"Сначала нужно окончить школу\nТебе осталось учиться {16 - age}")
        return False
    if "иван" in name.lower():
        return False
    return True

age = int(input())
name = input()
if isEntered(age, name):
    print("Поздравляем вы поступили в ВГУИТ")
    # последующая логика программы