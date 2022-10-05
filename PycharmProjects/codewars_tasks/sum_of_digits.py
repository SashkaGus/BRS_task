def sum_of_digits(num):
    str_num, a = str(num), 0
    if len(str_num)> 1:
        for i in str_num:
            a += int(i)
        return sum_of_digits(a)
    else:
        return num



print(sum_of_digits(132))