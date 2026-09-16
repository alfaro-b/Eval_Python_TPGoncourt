from daos.book_dao import BookDao
from daos.selection_dao import SelectionDao
from models.selection import Selection
from datetime import date

selection_dao = SelectionDao()

# Test read_all
print("----- READ ALL -----")
for selection in selection_dao.read_all():
    print(selection)

# Test read
print("\n----- READ -----")
print(selection_dao.read(1))

# Test d'un ID inexistant
print("\n----- READ INEXISTANT -----")
print(selection_dao.read(9999))

# Test create sur la BDD de test
print("\n----- CREATE -----")
selection_test = Selection(number=4,date=date(2026,9,15))
new_id = selection_dao.create(selection_test)
print(f"ID créé : {new_id}")
print(f"Objet : {selection_test}")
print(f"ID dans l'objet : {selection_test.id_selection}")

# Test ajout d'un livre à une sélection
print("\n----- ADD BOOK -----")
result = selection_dao.add_book(2, 2)
print(f"Ajout effectué : {result}")

book_dao = BookDao()
books = book_dao.read_by_selection(2)
for book in books:
    print(book.title)

print("Test : ajout d'un même livre une deuxième fois")
result = selection_dao.add_book(2, 2)
print(f"Ajout effectué : {result}")
