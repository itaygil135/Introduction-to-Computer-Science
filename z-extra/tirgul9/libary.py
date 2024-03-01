class Libary():
    def __init__(self):
        self.all_books = dict


    def add_book(self,book):
        if book.name not in self.all_books:
            self.all_books[book.name] = book

        else:
            new_copies = book.get_number_of_copies()
            self.all_books[book.name].add_copies(new_copies)

    def borrow_book(self,book):
        if book.name not in self.all_books:
            return False

        avaliable_copies = self.all_books[book.name].get_number_of_copies()
        if avaliable_copies == 0:
            return  False


        self.all_books[book.name].add_copies(-1)
        return True



    def __str__(self):
        collection_str = ''
        for book in self.all_books:
            collection_str += str (self.all_books[book]) + "\n"