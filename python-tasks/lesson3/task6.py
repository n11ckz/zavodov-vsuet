def isColorMatched(x1: int, y1: int, x2: int, y2: int) -> bool:
    if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
        return True
    if (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0:
        return True
    return False

if isColorMatched(3, 2, 6, 4):
    print("Да")
else:
    print("Нет")