class EditableString:
    def __init__(self, string):
        self.__string = list(string)
        self.__lst_args = []

    def insert_char_at(self, char1, ind):
        self.__lst_args.append([char1, ind])
        if (ind < 0) or (ind > len(self.__string)):
            raise IndexError
        elif ind == len(self.__string):
            self.__string.append(char1)
        else:
            temp = self.__string[:ind]
            temp.append(char1)
            self.__string = temp + self.__string[ind:]

    def delete_char_at(self, ind):
        self.__lst_args.append([ind])
        if (ind >= len(self.__string)) or (ind < 0):
            raise IndexError
        else:
            temp1 = self.__string[:ind]
            temp2 = self.__string[ind + 1:]
            self.__string = temp1 + temp2

    def redo_last_action(self):
        if not self.__lst_args:
            return

        my_args = self.__lst_args[-1]
        if len(my_args) == 2:
            self.insert_char_at(*my_args)
        else:
            self.delete_char_at(my_args[0])

    def __str__(self):
        my_string = ''
        for item in self.__string:
            my_string = my_string + item
        return my_string


estr = EditableString("poor")
estr.insert_char_at('t', 2)
estr.delete_char_at(1)
estr.redo_last_action()
print(str(estr))


def count_substrs(word):
    if len(word) == 1:
        return 1
    total = [0]
    my_dict = dict()
    # for letter in word:
    #    my_dict[letter] = 0
    return (count_substrs_helper(word, total, my_dict))


def count_substrs_helper(word, total, my_dict):
    if len(word) == 0:
        return
    else:
        count_substrs_helper(word[1:], total, my_dict)
        print("word= ", word)
        if word[0] in my_dict:
            my_dict[word[0]] = my_dict[word[0]] + 1
        else:
            my_dict[word[0]] = 1
        total[0] = total[0] + my_dict[word[0]]

    return total


count_substrs("abca")
# a, abca, b, bcab, c, a, b


'''class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def equal_trees(x, y):
    if x.data != y.data:
        return False
    else:
        return     ((equal_trees(x.left,y.left) and equal_trees(x.right, y.right))
                or (equal_trees(x.left,y.right) and equal_trees(x.right, y.left)))'''


'''def find_closest(lst, x):
    best = [lst[0],lst[1]]
    for i in range(2,len(lst)):
        find_best_comb(best,lst,i,x)


    best = tuple(best)
    return best
def find_best_comb(best,lst,i,x):
    dig = x - (best[1] + best[0])
    if dig < 0:
        dig = -1 * dig
    d = x - (lst[i] + best[0])
    if d < 0:
        d = -1 * d
    o = x - (best[1] + lst[i])
    if o < 0:
        o = -1 * o
    if d < o and d < dig:
        best[1] = lst[i]
    elif o < d and o < dig:
        best[0] = lst[i]
    else:
        pass
    return

print(find_closest([10, 22, 28, 29, 30, 40], 54))'''



'''
class Library:
def __init__(self):
    self.__books_dict = dict()
def add_book_copy(self, book_name: str) -> None
    if book_name in self.__books_dict:
        self.__books_dict[book_name][0] += 1
        self.__books_dict[book_name][1] += 1
    else:
        self.__books_dict[book_name] = [1,1]
def borrow_one_book(self, book_name: str) -> None
     if book_name not in self.__books_dict:
         raise ValueError
     elif  self.__books_dict[book_name][1] == 0:
         raise ValueError
     else:
         self.__books_dict[book_name][1] -= 1
def return_one_book(self, book_name: str) -> None
    if book_name not in self.__books_dict:
        raise ValueError
    elif self.__books_dict[book_name][0] == self.__books_dict[book_name][1]:
         raise ValueError
    else:
        self.__books_dict[book_name][1] += 1
def get_num_copies(self, book_name:str) -> int
    if book_name not in self.__books_dict:
        return 0
    else:
        return self.__books_dict[book_name][1]
        
        
        
        
        
        
def gen_str_helper(n):
    hold = []
    if n == 1:
        hold.append(str(0))
        hold.append(str(1))


    else:
        for item in gen_str_helper(n-1):
            if item[-1] == '1':
                hold.append(item +str(0))
            else:
                hold.append(item+str(0))
                hold.append(item+str(1))
    return hold


def gen_str(n):
    lst = gen_str_helper(n)
    for item in lst:
        print(item)

gen_str(3)
'''


initial_values = {"a": 5, "b": 1}
program = [("c", (lambda x, y: x * y), "a", "a"),
           ("c", (lambda x, y, z: x + y + z), "a", "b", "c"),
           ("return", "c")]
"suupost to return 31"

def evaluate(program, initial_values):
        for item in program:
            if type(item[0]) != "return":
                run_on_it = item[2:]
                my_args = [initial_values[arg] for arg in run_on_it]
                initial_values[item[0]] = item[1](*my_args)
            else:
                return initial_values[item[1]]

print(evaluate(program, initial_values))

"""def generate(n):
    if n>1:
        for i in generate(n-1):
            yield i*2
    yield 1
lst = list(generate(6))
print(*lst)

def compress(lst):
    l = []
    if len(lst) == 1:
        l.append((lst[0],1))
        return l
    n = 0
    for i in range(1,len(lst)):
        if lst[i-1] != lst[i]:
            l.append((lst[i-1],i - n))
            n = i
    if lst[-1] != lst[-2]:
        l.append((lst[-1],1))
    else:
        l.append((lst[-1],len(lst)-n))

    return l


import copy
def count_sums(a,s):
    all_subset = find_all_subset(a)
    print(all_subset)
    #return count_sums_helper(a,s,[],[])

def find_all_subset(a):
    if len(a) == 0:
        return [[]]
    first = a[0]
    a.remove(first)
    lst =[]
    for b in find_all_subset(a):
        lst.append(b)
        lst.append(b+[first])


    return lst

import copy
def count_sums(a,s):
    return count_sums_helper(a,s,[],[])

def count_sums_helper(a,s,sub,holding_lst):
    answer = is_valid(s,sub)
    if answer == "too much":
        return
    elif answer == "equal":
        val = copy.deepcopy(sub)
        holding_lst.append(val)

    for i in range(len(a)):
        sub.append(a[i])
        count_sums_helper(a[i+1:],s,sub,holding_lst)
        sub.pop()

    return len(holding_lst)



def is_valid(s,sub):
    if not sub:
        return False
    num = 0
    for item in sub:
        num = num + item
    if num == s:
        return "equal"
    elif num < s:
        return "keep going"
    else:
        return "too much"
"""




"""students_dict = dict()
class Student:
    def __init__(self,name):
        self.__name =name
        self.__stu_grades = []
        students_dict[name] = self

    def add_grade(self,value):
        self.__stu_grades.append(value)
        print(self.__stu_grades)
    def get_average(self):
        sum = 0
        for item in self.__stu_grades:
            sum = sum + item
        return sum/len(self.__stu_grades)

def get_student_by_name(name):
    return students_dict[name]
"""




"""class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


def zipper(head1, head2):
    cur = head1
    sec = head2
    hetz1 = cur
    hetz2 = sec
    while cur.next:
        hetz1 = hetz1.next
        hetz2 = hetz2.next
        cur.next = sec
        sec.next = hetz1
        sec = hetz2
        cur = hetz1
    cur.next = sec






nums_node = Node(1, Node(2, Node(3, Node(4))))
letters_node = Node("A", Node("B", Node("C", Node("D"))))
zipper(nums_node,letters_node)"""































"""
def get_reverse_iterator(head):
    cur = head
    rev_head = Node(head.data)
    while cur.next:
        rev_head = Node(cur.next.data, rev_head)
        cur = cur.next

    yield rev_head.data
    while rev_head.next:
        rev_head = rev_head.next
        yield rev_head.data

lst = Node("a",Node("b",Node("c",Node("d",Node("e",Node("f",Node("g",Node("h",Node("i")))))))))
for x in get_reverse_iterator(lst):
    print(x)"""

















'''class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def get_skip_iterator(self, skip):
        return SkipIterator(self.head, skip)


class SkipIterator:

    def __init__(self,head,skip=1):
        self.__head = head
        self.__skip = skip

    def __next__(self):
        if not self.__head:
            raise StopIteration
        res = self.__head
        for skip in range(self.__skip):
            if not self.__head:
                break
            self.__head = self.__head.next
        return res
    def __iter__(self):
        return self

L = LinkedList(Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7))))))))
for node in L.get_skip_iterator(2):
    print(node.get_data(), end=' ')'''
























"""import copy
def maximal_substring(str1,str2):
    str1 = list(filter(lambda x: x in str2,str1))
    str2 = list(filter(lambda x: x in str1, str2))
    str1 = ''.join(str1)
    str2 = ''.join(str2)

    if len(str2) < len(str1):
        short_str = copy.deepcopy(str2)
        long_str = copy.deepcopy(str1)
    else:
        short_str = copy.deepcopy(str1)
        long_str = copy.deepcopy(str2)

    ls = maximal_substring_helper(short_str,long_str,"",'')
    print(ls)

def maximal_substring_helper(short_str,long_str,longest_sub,mooving_str):
    if is_valid(mooving_str,long_str):
        if len(mooving_str) >  len(longest_sub):
            longest_sub = copy.deepcopy(mooving_str)
    for i in range(len(short_str)):
        mooving_str = mooving_str + short_str[i]
        longest_sub = maximal_substring_helper(short_str[i+1:],long_str,longest_sub,mooving_str)
        mooving_str = mooving_str[:-1]

    return longest_sub


def is_valid(mooving,long_str):
    cheking = ''
    for l in long_str:
        if l in mooving:
            cheking = cheking + l
    if cheking == mooving:
        return True
    else:
        return False"""


























"""

def blurg(seq):
    a = next(seq)
    yield a
    for b in seq:
        mid = (a+b)//2
        a=b
        yield mid
        yield b
my_iter=iter([0,8])
x1 =blurg(my_iter)
my_blurg = blurg(x1)
#print(list(my_blurg))
my_list = []
for item in my_blurg:
    my_list.append(item)
print(my_list)
"""