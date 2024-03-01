def change_list(lst):
    for i in range(len(lst)):
        lst[i] = 2 * lst[i]

    return 1.618


def permutations_dist_helper(word,dist,all_options,mila):
    if len(word)==0:
        all_options.append(mila)
        return

    for ind, item in enumerate(word):
        if ok_to_place(mila,item, dist):
            mila = mila + item
            new_word = word[0:ind]+word[ind+1:]
            permutations_dist_helper(new_word,dist,all_options,mila)
            mila = mila[:-1]
    return all_options


def ok_to_place(mila,item,dist):
    if len(mila) == 0:
        return True

    num = ord(item) - ord(mila[-1])
    if num == 0:
        return True

    if num > 0 :
        if num <= dist:
            return True
        else:
            return False

    num = -1 * num
    if num <= dist:
        return True
    else:
        return  False



def permutations_dist(word, dist):
    if len(word) == 0:
        return 1
    all_options = []
    some = ""
    all_options = permutations_dist_helper(word,dist,all_options,some)
    return len(all_options)


print(permutations_dist('abcd',1))