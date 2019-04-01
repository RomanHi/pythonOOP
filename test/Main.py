
class BookCalc(object):
    books = {}

    def __init__(self, input_str='Hello, World'):
        print("init class")
        self.books = dict(input_str[i:i + 2] for i in range(0, len(input_str), 2))
        for key, value in self.books.items():
            self.books.update([key, int(self.books.get(key))])

    def __del__(self):
        del self.books

    def get_book(self, book_name):
        self.books[book_name] -= 1
        return self.books[book_name]

    def set_book(self, book_name):
        self.books[book_name] += 1
        return self.books[book_name]




