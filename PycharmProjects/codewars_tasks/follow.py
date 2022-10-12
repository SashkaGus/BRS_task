def follow(instructions:str):
    a, b, arr = 0, 0, [i for i in instructions]
    print(arr)
    for i in arr:
        match i:
            case 'f':
                b += 1
            case 'b':
                b -= 1
            case 'r':
                a += 1
            case 'l':
                a -= 1
    return (a, b)


print(follow("ffrff"))