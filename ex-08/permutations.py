


def _print_all_perm_helper(lst,ind):
    if ind == len(lst) - 1:
        print(lst)
        return

    _print_all_perm_helper(lst, ind + 1)

    for i in range (ind +1, len(lst)):
        lst[ind], lst[i] = lst[i], lst[ind]
        _print_all_perm_helper(lst, ind + 1)
        lst[ind], lst[i] = lst[i], lst[ind]


def _return_all_perm_helper(lst,result, ind):
    if ind == len(lst) - 1:
        result.append(lst[:])
        return

    _return_all_perm_helper(lst, result , ind + 1)

    for i in range (ind +1, len(lst)):
        lst[ind], lst[i] = lst[i], lst[ind]
        _return_all_perm_helper(lst,result, ind + 1)
        lst[ind], lst[i] = lst[i], lst[ind]


def print_all_permutations(lst):
    _print_all_perm_helper(lst,0)


def return_all_permutations(lst):
    result = []
    _return_all_perm_helper(lst, result, 0)
    return result


if __name__ == '__main__':

    lst = ["a","b","c"]
    print("calling helper that print")
    print_all_permutations((lst))

    print("calling helper that return list")
    result = return_all_permutations((lst))
    print(result)