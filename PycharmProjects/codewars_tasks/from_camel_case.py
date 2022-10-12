def from_camel_case(text:str):
    big_alph = "abcdefghijklmnopqrstuvwxyz".upper()
    new_str = ''
    for i in text:
        if i in big_alph:
            new_str += '_' + i.lower()
        else:
            new_str += i
    return new_str if new_str[0] != '_' else new_str[1:]

print(from_camel_case('CamelCase'))
