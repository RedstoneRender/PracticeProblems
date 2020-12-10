def alternateCase(str):
    newStr = ""
    for i in range(len(str)):
        char = str[i]
        if i%2 == 0:
            if char.upper() == char:
                char = char.lower()
            else:
                char = char.upper()
        newStr+=char
    return newStr
