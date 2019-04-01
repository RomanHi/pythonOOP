class Books(object):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def display_book(self, book):
        self.book = book
        return self.book

    def take_one_book(self, book):
        self.book = book - 1
        return self.book

    def put_one_book(self, book):
        self.book = book + 1
        return self.book


a = Books()

new_list = list(input().split())

for i in new_list:
    if i.isalpha():
        print(i, end=" ")
    if i.isdigit():
        print(a.display_book(int(i)), end=" ")
        print(a.take_one_book(a.display_book(int(i))), end=" ")
        print(a.put_one_book(a.take_one_book(a.display_book(int(i)))), end=" ")

