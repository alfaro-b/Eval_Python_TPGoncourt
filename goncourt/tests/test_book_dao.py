from daos.book_dao import BookDao
from models.book import Book
from datetime import date

book_dao = BookDao()

# Test read_all
print("----- READ ALL -----")
for book in book_dao.read_all():
    print(book)

# Test read
print("\n----- READ -----")
print(book_dao.read(1))

# Test d'un ID inexistant
print("\n----- READ INEXISTANT -----")
print(book_dao.read(9999))

# Test create sur la BDD de test
print("\n----- CREATE -----")
book_test = Book(title='test', summary='ekfherahfariughal', publication_date=date(2026, 9, 15), nbr_pages=150,
                 isbn='1234567891234', publisher_price=10.50, id_author=1, id_publisher=1)
new_id = book_dao.create(book_test)
print(f"ID créé : {new_id}")
print(f"Objet : {book_test}")
print(f"ID dans l'objet : {book_test.id_book}")

print("\n----- READ BY SELECTION -----")

books = book_dao.read_by_selection(1)

for book in books:
    print(book.title)

print("\n----- READ BY SELECTION VIDE -----")

books = book_dao.read_by_selection(2)

print(books)
