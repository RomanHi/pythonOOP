import hashlib


class BookRepository(object):
    books = {}

    def __init__(self, input_str='Hello, World'):
        split = input_str.split()
        self.books = dict(split[i:i + 2] for i in range(0, len(split), 2))
        for key, value in self.books.items():
            self.books[key] = int(value)

    def print_result(self):
        for key in sorted(self.books):
            print(key + ' ' + str(self.books[key]), end="\n")


class HashMd5(BookRepository):

    def __init__(self, enc, books):
        self.enc = enc
        self.books = books
        super(BookRepository, self).__init__()

    def getHash(self):
        for key in sorted(self.books):
            print("md5", hashlib.md5(key.encode()).hexdigest(), end=" ")


new_list = input()
enc = input()
a = BookRepository(new_list)
a.print_result()
b = HashMd5(enc, a.books)
b.getHash()