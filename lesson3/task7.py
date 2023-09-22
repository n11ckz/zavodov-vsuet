def isYearLeap(year) -> bool:
    if year % 4 == 0 or year % 400 == 0:
        return True
    return False

currentYear = 2023
if isYearLeap(currentYear):
    print(f"{currentYear} - leap year")
else:
    print(f"{currentYear} - non-leap year")