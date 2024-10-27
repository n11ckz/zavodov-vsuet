def isYearLeap(year: int) -> bool:
    if year % 4 == 0 or year % 400 == 0:
        return True
    return False

currentYear: int = 2023
if isYearLeap(currentYear):
    print(f"{currentYear} - високосный год")
else:
    print(f"{currentYear} - невисокосный год")