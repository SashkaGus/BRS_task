def checkio(line1: str, line2: str) -> str:
    fisrt, second, result = [], [], []
    first = line1.split(',')
    second = line2.split(',')
    for i in first:
        for j in second:
            if i == j:
                result.append(i)
    res = sorted(result)
    return ','.join(res)


print(checkio("one,two,three", "four,five,one,two,six,three"))