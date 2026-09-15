from daos.publisher_dao import PublisherDao
from models.publisher import Publisher


publisher_dao = PublisherDao()

# Test read_all
print("----- READ ALL -----")
for publisher in publisher_dao.read_all():
    print(publisher)

# Test read
print("\n----- READ -----")
print(publisher_dao.read(1))

# Test d'un ID inexistant
print("\n----- READ INEXISTANT -----")
print(publisher_dao.read(9999))

# Test create sur la BDD de test
print("\n----- CREATE -----")
publisher_test = Publisher(name="Éditeur test")
new_id = publisher_dao.create(publisher_test)
print(f"ID créé : {new_id}")
print(f"Objet : {publisher_test}")
print(f"ID dans l'objet : {publisher_test.id_publisher}")