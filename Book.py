"""Book example"""

class Book:
    total_number_of_books = 0

    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        Book.total_number_of_books += 1
        self.id = Book.total_number_of_books

if __name__ == '__main__':
    print(Book.total_number_of_books)
    tadeusz = Book('Pan Tadeusz', 'Adam Mickiewicz', 200)
    print(Book.total_number_of_books)
    print(f'TITLE: {tadeusz.title} ID: {tadeusz.id}')