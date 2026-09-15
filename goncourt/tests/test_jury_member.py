from daos.jury_member_dao import JuryMemberDao
from models.jury_member import JuryMember


jury_member_dao = JuryMemberDao()

# Test read_all
print("----- READ ALL -----")
for jury_member in jury_member_dao.read_all():
    print(jury_member)

# Test read
print("\n----- READ -----")
print(jury_member_dao.read(1))

# Test d'un ID inexistant
print("\n----- READ INEXISTANT -----")
print(jury_member_dao.read(9999))

# Test read_president
print("\n----- READ PRESIDENT -----")
print(jury_member_dao.read_president())

# Test create sur la BDD de test
print("\n----- CREATE -----")
jury_member_test = JuryMember(
    last_name="Test",
    first_name="Jury",
    is_president=False
)

new_id = jury_member_dao.create(jury_member_test)

print(f"ID membre du jury créé : {new_id}")
print(f"ID personne : {jury_member_test.id_person}")
print(f"ID membre du jury : {jury_member_test.id_jury_member}")
print(f"Objet : {jury_member_test}")