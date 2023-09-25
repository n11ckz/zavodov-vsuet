def isColorMatched(x1, y1, x2, y2) -> bool:
    if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
        return True
    if (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0:
        return True
    return False

if isColorMatched(3, 2, 6, 4):
    print("Yes")
else:
    print("Nope")