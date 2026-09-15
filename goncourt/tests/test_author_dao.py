from daos.author_dao import AuthorDao
from models.author import Author

author_dao = AuthorDao()

# Test read_all
print("----- READ ALL -----")
for author in author_dao.read_all():
    print(author)

# Test read
print("\n----- READ -----")
print(author_dao.read(1))

# Test d'un ID inexistant
print("\n----- READ INEXISTANT -----")
print(author_dao.read(9999))

# Test create sur la BDD de test
print("\n----- CREATE -----")
author_test = Author(
    last_name='test',
    first_name='Auteur',
    biography='hcufruféihgvkr'
)
new_id = author_dao.create(author_test)
print(f"ID auteur créé : {new_id}")
print(f"ID personne créé : {author_test.id_person}")
print(f"Objet : {author_test}")
print(f"ID author dans l'objet : {author_test.id_author}")
