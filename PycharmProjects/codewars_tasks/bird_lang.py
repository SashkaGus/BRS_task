from hashlib import new


def translate(text:str):
    vowel_let, arr, str_len, new_text, res = 'aeiouy', [], range(len(text)), list(text.strip()), []
    for i in str_len:
        if text[i] == ' ':
            continue
        elif text[i] not in vowel_let:
            arr.append(i + 1)
    for idx, ele in enumerate(new_text):
        if idx not in arr:
            res.append(ele)
    for i in range(len(res)):
        if res[i] in vowel_let:
            try:
                res[i+1], res[i+2] = '1', '1'
            except IndexError:
                continue
    result = []
    for i in res:
        if i != '1':
            result.append(i)
    return ''.join(result)

print(translate("aaa bo cy da eee fe"))