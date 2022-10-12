def sum_by_types(items: list[str, int]) -> tuple[str, int] | list[str, int]:
    sum_res, str_res = 0, ''
    for i in items:
        if type(i) is int:
            sum_res += i
        if type(i) is str:
            str_res += i
    return [str_res, sum_res]

print(sum_by_types(["size", 12, "in", 45, 0]))