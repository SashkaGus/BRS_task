from os import dup


def duplicate_zeros(lst:list):
    ind_arr, a = [], 0
    for i, j in enumerate(lst):
        if j == 0:
            ind_arr.append(i)
    for i in ind_arr:
        lst.insert(i + a, 0)
        a += 1
    return lst


print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicate_zeros([0,0,0,0]))
