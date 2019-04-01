class BookCalc(object):
    books = {}

    def __init__(self, input_str='Hello, World'):
        split = input_str.split()
        self.books = dict(split[i:i + 2] for i in range(0, len(split), 2))
        for key, value in self.books.items():
            self.books[key] = int(value)

    def __del__(self):
        del self.books

    def pop_book(self, book_name):
        self.books[book_name] -= 1
        return self.books[book_name]

    def set_book(self, book_name):
        self.books[book_name] += 1
        return self.books[book_name]

    def get_book(self, book_name):
        return self.books.get(book_name)

    def print_result(self):
        for key, value in self.books.items():
            print(key +' '+str(value)+' '+str(self.pop_book(key))+' '+str(self.set_book(key)))


input_str = input()
a = BookCalc(input_str)
a.print_result()
