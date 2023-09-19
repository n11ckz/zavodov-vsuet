def calculateHours(minutes) -> int:
    return minutes // 60

def calculateMinutes(minutes) -> int:
    return minutes % 60

def showTime(minutes) -> None:
    if minutes < 0 and minutes >= 1440:
        return
    print(f"{calculateHours(minutes)}:{calculateMinutes(minutes)}")

print(showTime(820))