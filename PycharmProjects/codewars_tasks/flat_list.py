import itertools
def flat_list(arr):
    res = []
    str_arr = str(arr)
    new_str = str_arr.replace('[', '').replace(']', '')
    res = new_str.split(',')
    for i in res:
        if i == ' ':
            res.remove(i)
    return [int(i) for i in res] if new_str else []


print(flat_list([-1,[1,[-2,[3],[[5],[10,-11],[1,100,[-1000,[5000]]],[20,-10,[[[]]]]]]]]))