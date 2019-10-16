"""
Book example
"""
isbn_db = {
    'ABC123': ('Pan Tadeusz', 'Adam Mickiewicz'),
    'ABC124': ('Zawód Programista', 'Maciej Aniserowicz'),
    'ABC125': ('DNA', 'Maciej Aniserowicz'),
}

class Book:
    total_number_of_books = 0

    def __init__(self, title, author, ):
        self.title = title
        self.author = author
        Book.total_number_of_books += 1
        self.id = Book.total_number_of_books

    @classmethod
    def from_isbn(cls, isbn):
        title, author = isbn_db.get(isbn)
        return Book(title, author)

if __name__ == '__main__':
    new_book = Book.from_isbn('ABC123')

    isbns = ['ABC123', 'ABC124', 'ABC125',]
    books = []
    for isbn in isbns:
        books.append(Book.from_isbn(isbn))