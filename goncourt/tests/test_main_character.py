from daos.main_character_dao import MainCharacterDao
from models.main_character import MainCharacter


main_character_dao = MainCharacterDao()

# Test read_all
print("----- READ ALL -----")
for main_character in main_character_dao.read_all():
    print(main_character)

# Test read
print("\n----- READ -----")
print(main_character_dao.read(1))

# Test d'un ID inexistant
print("\n----- READ INEXISTANT -----")
print(main_character_dao.read(9999))

# Test create sur la BDD de test
print("\n----- CREATE -----")
main_character_test = MainCharacter(
    name="Personnage test",
    id_book=1
)

new_id = main_character_dao.create(main_character_test)

print(f"ID créé : {new_id}")
print(f"ID dans l'objet : {main_character_test.id_main_character}")
print(f"Objet : {main_character_test}")

# Test read_by_book
print("\n----- READ BY BOOK -----")
characters = main_character_dao.read_by_book(1)

for character in characters:
    print(character)