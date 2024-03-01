

def power_set(A):
    if len(A) == 0:
        return[[]]

    x_1 = A[0]
    without_x_1 = A[:]
    without_x_1.remove(x_1)
    all_subsets = []
    for subset in power_set(without_x_1):
        all_subsets.append(subset)
        all_subsets.append(subset + [x_1])
    return all_subsets

if __name__ == '__main__':
    A = [2, 9, 3, 23, 0, None, 1, -1, True]
    print(len(power_set(A)))