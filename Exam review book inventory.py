
class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity= quantity
    
    def update_quantity(self, amount):
        self.quantity += amount
    
class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        self.books.remove(book)

    def display_inventory(self):
        for book in self.books:
            print(book.title, book.author, book.price, book.quantity)

if __name__ == "__main__":
    bookstore = BookStore()


book1 = Book("heart of a lion", "Giliad", 10, 5)
book2 = Book("Freedom", "James Baldwin", 13, 15)


bookstore.add_book(book1)
bookstore.add_book(book2)


bookstore.display_inventory()


