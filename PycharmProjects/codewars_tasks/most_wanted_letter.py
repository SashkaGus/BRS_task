from hashlib import new
from typing import Collection


def checkio(text_inp:str):
    text = text_inp.lower()
    from collections import Counter
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    a, b = Counter(text.lower()), ''
    for i in text:
        if i in alphabet:
            b += i
    a = Counter(b)
    max_val = max(a.values())
    new_arr = a.values()
    # print(list(new_arr))
    arr_val = [list(a.values()).index(max_val)]
    # print(arr_val)
    if len(set(a.values())) > 1:
        if list(a.values()).count(max_val) > 1:
           return sorted([k for k,v in a.items() if v == max_val])[0]
        else:
           return max(a, key=a.get)
    else:
        return sorted(a.keys())[0]


print(checkio("Lorem ipsum dolor sit amet"))