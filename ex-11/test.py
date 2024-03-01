'''def mat_gen():
    my_counter = []


    def g(mat):
        if mat == []:
            yield [[]]
        row = 0
        col = 0
        l = len(mat[0])
        while  row < len(mat) and col < len(mat[0]):
            my_counter.append("I")
            if len(my_counter) % 2 == 0:
                cil = []
                for i in range(row,len(mat)):
                    cil.append(mat[i][col])
                yield cil
                col = col +1
            else:
                x = mat[row]
                yield x[col:l]
                row = row + 1

    return g


mat = [[1,2,3,4],[2,8,6,4],[5,1,7,9]]
g = mat_gen()(mat)

#for i in g:
#    print(i)

try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    pass

'''
























'''class Sorting:
    def __init__(self,):
        self._head = None
        self._next = None
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        #self.head = data
    def push(self,value):
        self.data = self.head


def get_min(lst):
    # get the minimal value at the list
    min = lst[0]
    for i in range(len(lst)):
        if min > lst[i]:
            min = lst[i]
    return min

def get_max(lst):
    # get the minimal value at the list
    maxval = lst[0]
    for i in range(len(lst)):
        if maxval < lst[i]:
            maxval = lst[i]
    return maxval


def get_next_min(lst, min, maxval):
    # get the minimal value at the list, but it should be greater then min
    next_min = maxval
    for i in range(len(lst)):
        if lst[i] > min and lst[i] < next_min:
            next_min = lst[i]
    return next_min


def go_over_in_order(iterable):

    maxval = get_max(iterable)
    min = get_min(iterable)

    yield min  # print the first minimal element
    for i in range(1,len(iterable)):
        next_min = get_next_min(iterable,min,maxval)
        yield next_min
        min = next_min


#print(list(go_over_in_order([91,6,8,3,2,66,45,1])))

my_iter = iter(go_over_in_order([91,6,8,3,2,66,45,1]))
print(next(my_iter))
'''






















'''class MyMaplter:

    def __init__(self,f,*args):
        self._f = f
        self._args = args

    def __next__(self):
        my_lst =[]
        for it in self._args:
            try:
                my_lst.append(next(it))
            except StopIteration:
                break

        return self._f(*my_lst)


    def __iter__(self):
        return self

func1 = lambda x,y,z: str(x) + str(y) + str(z)
iter1 = iter(range(10))
iter2 = iter(range(5))
iter3 =(i**2 for i in range (4))
for i in MyMaplter(func1, iter1 , iter2 ,iter3):
    print(i)'''










'''
class Tree:
    def __init__(self, value, branches=[]):
        self.value = value
        self.branches = list(branches)


def depth_n_node(tree, n):
    if n == 0:
        yield tree.value
    else:
        for branch in tree.branches:
            yield from depth_n_node(branch, n - 1)
    return


def bfs_order(tree):
    n = 0 #to get dept
    count = 1
    while count > 0:
        count = 0
        if n == 2:
            print(n)
        for node in depth_n_node(tree, n):
            yield node
            count += 1
        n += 1




print(list(bfs_order(Tree(1,
                          [Tree(2, [Tree(5), Tree(6)]) ,
                           Tree(3, [Tree(7)]),
                           Tree(4, [Tree(8)])]))))'''
























'''def pasc_row(n):
    current_row = create_line_n(n)
    yield current_row
    while True:
        next_row = calculate_next_row(current_row)
        current_row = next_row
        yield next_row

        #n=2 i =2,j=1
        #n = 3 (i=3,j=1)(i=3,j=2)
        #  get the line for (n-1)
        #  L[0] = 1 , L[n-1] =1 ,  for j in range(1:n-1):
        #                              calculate L[n][j]
def calculate_next_row(current_row):
    next_row= [1]
    for i in range(1,len(current_row)):
        next_row.append(current_row[i-1] + current_row[i])
    next_row.append(1)
    return next_row

def create_line_n(n):
    if n == 0:
        return [1]
    else:
        prev_row = create_line_n(n-1)
        current_row = calculate_next_row(prev_row)
        return current_row



g = pasc_row(3)
print(next(g))
print(next(g))'''


'''class Dropwhile:

    def __init__(self,f,it):
        self._f = f
        self._it = it
        self._situation = True

    def __next__(self):
        x = next(self._it)
        while self._situation:
            if not self._f(x):
                self._situation = False
            else:
                x = next(self._it)
        if self._situation == False:
           return x


    def __iter__(self):
        return self


f = lambda x: x<30
i = iter([11,2,3,4,5,0,1])
lst = list(Dropwhile(f,i))
print(lst)


def count_to(num):
    if num <= 0:
        return
    for i in count_to(num-1):
        yield i
    yield num

x = count_to(3)
print(next(x))
print(next(x))
'''