def f(lst):
    return [(x // 3) + (x**2) for x in range(len(lst) - 1, 0, -1) if lst[x] % 2 == 0 and lst[x] < 30]

print(f([80, 60, 20, 10, 5]))






def make_pretty(func):

    def new_func(*args):
        print("i am got decorated")
        func()
        return new_func



    return(new_func)


@make_pretty
def ordinary():
    print("I am ordinary")


'''def min_chars(s1, s2):
    if s1 in s2:
        return 0
    elif not s1:
        return 0
    elif len(s2) == 1:
        return 1
    return 1 + min_chars(s1[1:], s2[1:])

print(min_chars("cdef", "abzdef"))
print(min_chars("abc", "azbzc"))
print(min_chars("abc", "pdxzk"))'''














