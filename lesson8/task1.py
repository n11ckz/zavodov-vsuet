# вариант 2
def calculateAreaOfEquilateralTriangle(a: float) -> float:
    return ((a ** 2) * (3 ** 0.5)) / 4

def calculateAreaOfRegularHexagon(a: float) -> float:
    triangleSquare = calculateAreaOfEquilateralTriangle(a)
    return triangleSquare * 6

print(f"{calculateAreaOfRegularHexagon(10):.3f}")