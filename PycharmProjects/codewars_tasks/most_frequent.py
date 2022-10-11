def goes_after(word:str, first:str, second:str):
    try:
        a = word.index(first)
        b = word.index(second)
    except ValueError:
        return False
    if a + 1 == b:
        return True
    else:
        return False

print(goes_after("list", "l", "o"))