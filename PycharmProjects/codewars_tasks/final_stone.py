from re import A


def final_stone(arr):
    sort_arr = sorted(arr)
    if len(sort_arr) > 1 :
        last_val = sort_arr.pop(-1) - sort_arr.pop(-1)
        sort_arr.append(last_val)
        return final_stone(sort_arr)
    return sort_arr[0] if sort_arr else 0



print(final_stone([]))