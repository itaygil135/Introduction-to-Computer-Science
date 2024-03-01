def func_3(lst, index):
    return lst[index] +1
def func_2(lst,index):
    try:
        print(func_3(lst,index), end =" ")
    except IndexError:
        print("Error A", end= " ")
    except TypeError:
        print("error B", end= " ")

def func_1():
    lst = [0, 1, "2", 3]
    for i in range(len(lst) + 1):
        func_2(lst, i)

func_1()