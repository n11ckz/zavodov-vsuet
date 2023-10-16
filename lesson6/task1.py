# вариант 2
def replaceChars(string: str, replacedChar: str = ':', newChar: str = '%') -> None:
    newString = string.replace(replacedChar, newChar)
    print(f"{newString}\n{newString.count(newChar)}")

message = ".::_T:T_::."
replaceChars(message)