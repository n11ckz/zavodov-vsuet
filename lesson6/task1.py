# вариант 2
def replaceChars(string: str, replacedChar: str = ':', newChar: str = '%') -> None:
    newString: str = string.replace(replacedChar, newChar)
    print(f"{newString}\n{newString.count(newChar)}")

message: str = ".::_T:T_::."
replaceChars(message)