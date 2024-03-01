def count_sums(a,s):
    all_subsets = power_set(a)
    count = 0
    for sub in all_subsets:
        if sum(sub) == s:
            count += 1
    return count



def power_set(a):
    if len(a) == 0:
        return [[]]

    x_1 = a[0]

    a.remove(x_1)
    all_subset = []
    for subset in power_set(a):
        all_subset.append(subset)
        all_subset.append(subset + [x_1])
    return all_subset


print(count_sums([3,5,8,9,11,12,20],20))
















def all_increasing(lst):
    all_increasing_helper(lst, [])


def all_increasing_helper(lst,subset):
    if is_valid(subset):
        print(subset, end=" ")
    else:
        return

    for i in range(len(lst)):
        subset.append(lst[i])
        all_increasing_helper(lst[i+1:], subset)
        subset.pop()

def is_valid(lstt):
    if len(lstt) == 0:
        return True
    num = lstt[0]
    for i in range(len(lstt)):
        if num > lstt[i]:
            return False
        num = lstt[i]

    return True



class Node:
 def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def init_list(self,node_list):
        self.__head = node_list
        self.__tail = self.__head
        while self.__tail.next != None:
            self.__tail = self.__tail.next
    def is_repetative(self,lst):
        i = 0
        cur = self.__head
        while cur.data == lst[i]:
            if cur == self.__tail:
                if i == len(lst) -1:
                    return True
                else:
                    return False
            i = i +1
            if i == len(lst):
                i = 0
            cur = cur.next
        else:
            return False
'''
my_node = Node("b")
node = Node("a",my_node)
gaga = Node("b",node)
shmuel = Node("a",gaga)
kookoo = Node("b",shmuel)
lala = Node("a",kookoo)
myList = LinkedList()
myList.init_list(lala)


print(myList.is_repetative(["a", "b"]))
print(myList.is_repetative(["a", "b", "a"]))
print(myList.is_repetative(["a", "b", "a", "b"]))
print(myList.is_repetative(["c"]))'''



def find_discontinuity(lst):
    start = 0
    end = len(lst) - 1
    ind = (end + start) // 2
    if lst[start] > lst[start+1]:
        return start
    return find_discontinuity_helper(lst, start, end, ind)



def find_discontinuity_helper(lst, start, end, ind):

    if lst[ind] > lst[ind + 1] and lst[ind] > lst[ind - 1]:
        return ind
    elif lst[ind] < lst[end]:
        end = ind
    else:
        start = ind
    ind = (start + end) // 2
    return find_discontinuity_helper(lst, start, end, ind)



def f(x,n):
    return  (x + 1)% 7

def inverse(f,n):
    my_dict = dict()
    for i in range(n):
        my_dict[f(i)] = i
    def func(f,n):
        return func(**kargs(*args))

    return func

'''g = inverse(f,n)
print(g(3))'''
def most_common(lst):
    i = 0
    my_dict = dict()
    max = lst[0]
    while i < len(lst):
        if lst[i] in my_dict:
            my_dict[lst[i]] = my_dict[lst[i]] +1
        else:
            my_dict[lst[i]] = 1

        if my_dict[lst[i]] > my_dict[max]:
            max = lst[i]
        i = i +1

    return max



'''print(most_common(["alice"]))'''
print(tuple(range(5)))


