class Book:

    library_name = "市图书馆"

    def __init__(self, name: str, author: str, is_borrowed: bool=False):
        self.name = name
        self.author = author
        self.__is_borrowed = is_borrowed

    @property
    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        if self.is_borrowed:
            raise ValueError("图书已被借出")
        self.__is_borrowed = True

    def return_book(self):
        self.__is_borrowed = False

    def __str__(self):
        return (f"[{self.library_name}] {self.name} - {self.author} - {self.__is_borrowed}")

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author

    def __hash__(self):
        return hash((self.name, self.author))

b1 = Book("活着", "余华")
b2 = Book("活着", "余华")
b3 = Book("三体", "刘慈欣")
print(b1 == b2)   # 应该是 True
print(b1 == b3)   # 应该是 False

books = {b1, b2, b3}
for book in books:
    print(book)
