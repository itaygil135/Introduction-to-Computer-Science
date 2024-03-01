class Node:
    def __init__(self, data=None, next=None):
        self.__data = data
        self.__next = next

    def __str__(self):
        return str(self.__data)

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, data):
        self.__data = data

    def set_next(self, next):
        self.__next = next


class LinkedList():
    def __init__(self):
        self.__head = None

    def add(self, value):
        new_head = Node(value)
        new_head.set_next(self.__head)
        self.__head = new_head

    def __str__(self):
        result = "head"
        node = self.__head
        while node:
            result += " -> " + str(node)
            node = node.get_next()
        return result + " -> None"

    ####### Q1 #########
    def remove_data_by_idx(self, idx):
        if idx < 0:
            raise IndexError("idx must be non-negative")
        current = self.__head
        previous = None
        for _ in range(idx):
            if current is None:
                break
            previous = current
            current = current.get_next()
        if current is None:
            raise IndexError("the empty is shot then yor idx")
        if previous is None:
            self.__head = current.get_next()
            return
        else:
            previous.set_next(current.get_next())

    ####### Q2 #########
    def remove(self, data):
        current = self.__head
        previous = None
        if current == None:
            return "the list is empty"
        while current.get_next():
            if current.get_data() == data:
                if previous == None:
                     self.__head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()
        if current.get_data() == data:
            if previous == None:
                self.__head = None
                return
            previous.set_next(None)
            return
    ####### Q3 #########
    def remove_all(self, data):
        current = self.__head
        previous = None
        if current == None:
            return "the list is empty"
        while current.get_next():
            if current.get_data() == data:
                previous.set_next(current.get_next())
            else:
                previous = current
            current = current.get_next()
        if current.get_data() == data:
            if previous == None:
                self.__head = None
                return
            previous.set_next(None)
            return


if __name__ == '__main__':
    lst = LinkedList()
    lst.add(0)
    lst.add(1)
    lst.add(2)
    lst.add(2)
    lst.add(3)
    lst.add(1)
    lst.add(0)
    print("###############Q1#################")
    print(lst)
    print("Removing first element:")
    lst.remove_data_by_idx(0)
    print(lst)
    print("Removing last element:")
    lst.remove_data_by_idx(5)
    print(lst)
    print("###############Q2#################")
    print(lst)
    print("Removing 1 once:")
    lst.remove(1)
    print(lst)
    print("###############Q3#################")
    lst.add(1)
    print(lst)
    print("Removing all 2 occurrences:")
    lst.remove_all(2)
    print(lst)
    print("################################")