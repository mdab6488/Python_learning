# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are autonatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book(title="The Hobbit", author="J.R.R Tolkien", num_pages=310)
# book2 = Book(title="The Hobbit", author="J.R.R Tolkien", num_pages=310)
book2 = Book(title="Harry Potter and The Philosopher's Stone", author="J.K Rowling", num_pages=223)
book3 = Book(title="The Lion, the Witch and the Wardrobe", author="C.S. Lewis", num_pages=172)

print("*" * 30)
print(f"{' ' * 10} __init__ {' ' * 10}")
print("*" * 30)
# print(book1) # <__main__.Book object at 0x000001DAF8276900>
print("<__main__.Book object at 0x000001DAF8276900>")
print()

print("*" * 30)
print(f"{' ' * 10} __str__ {' ' * 10}")
print("*" * 30)
print(book1)
print(book2)
print(book3)
print()
print(book1 == book2)
print(book2 < book3)
print(book2 > book3)
print(book2 + book3)
print()
print("Lion" in book3)
print(book2['title'])
print(book2['author'])
print(book2['num_pages'])
print(book2['audio'])

