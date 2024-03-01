def generate_divisors(n):
    i = 0
    for i in range(1, n // 2 +i):
        if n % i ==0:
            yield item
        else:
            yield n


def generate_squares():
    x1 =0
    while True
        yield x1*x1
        x1 += 1


class ListEvenRevIter:
    def __init__(self,my_list):
        self._my_list = my_list
        self.i = len(self._my_list) -1
        if self.i % 2 != 0:
            self.i = self.i -1

    def __iter__(self):
        return self
    def __next__(self):

        yield self._my_list[self.i]
        self.i = self.i -2




def generate_n(n):
    if n < 1:
        raise StopIteration ('not supported')
    elif n == 1:
        yield n
    else:
        generate_n(n-1)
        yield n

#


def generate_n_rev(n):
    if n >=1:
        yield n
       for i in generate_n(n - 1):
           yield from i



def generate_max_to_min(root):
    pass


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __iter__(self):
        return generate_max_to_min(self)


if __name__ == "__main__":
    #Q1
    num = 24
    div_num_gen = generate_divisors(num)
    #for div in div_num_gen:
    #    print (div)
    #print ()

    #Q2
    s = 0
    gen_squares = generate_squares()
    #while s <= 10:
    #    print (next(gen_squares))
    #    s += 1

    # Q3
    lst1 = [4,3,2,5,6,7,3,2,1,4,6,7]
    lst2 = [4,3,2,5,6,7,3,2,1,4,6]
    #lst1_iter = ListEvenRevIter(lst1)
    #lst2_iter = ListEvenRevIter(lst2)
    #for elem in lst1_iter:
    #    print (elem)
    #print ()
    #for elem in lst2_iter:
    #    print (elem)

    #Q4
    num = 10
    num_gen = generate_n(num)
    #for j in num_gen:
    #    print (j)
    num_gen_rev = generate_n_rev(num)
    #for j in num_gen_rev:
    #    print (j)

    #Q5
    n7 = Node(7)
    n5 = Node(5)
    n6 = Node(6, n5, n7)
    n3 = Node(3)
    n1 = Node(1)
    n2 = Node(2, n1, n3)
    n4 = Node(4, n2, n6)
    #for j in n4:
        #print (j)
