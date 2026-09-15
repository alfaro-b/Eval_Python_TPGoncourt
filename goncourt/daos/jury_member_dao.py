# -*- coding: utf-8 -*-

"""
Classe Dao[JuryMember]
"""
from models.jury_member import JuryMember
from daos.dao import Dao
from dataclasses import dataclass


@dataclass
class JuryMemberDao(Dao[JuryMember]):
    def read_all(self) -> list[JuryMember]:
        jury_members: list[JuryMember] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    SELECT 
                        jury_member.id_jury_member,
                        jury_member.is_president,
                        person.id_person,
                        person.last_name,
                        person.first_name                         
                    FROM jury_member
                    JOIN person ON person.id_person = jury_member.id_person
                """
                cursor.execute(sql)
                records = cursor.fetchall()

                for record in records:
                    jury_member = JuryMember(
                        id_jury_member=record['id_jury_member'],
                        is_president=record['is_president'],
                        id_person=record['id_person'],
                        last_name=record['last_name'],
                        first_name=record['first_name']
                    )
                    jury_members.append(jury_member)
            except Exception as error:
                print(f"Erreur lors de la lecture des membres du jury {error}")

        return jury_members

    def create(self, jury_member: JuryMember) -> int | None:
        """Crée en BD l'entité JuryMember correspondant à jury_member

        :param jury_member: membre du jury à créer en BDD sous forme d'entité jury_member
        :return: l'id de l'entité insérée en BDD
        """
        with Dao.connection.cursor() as cursor:
            try:
                # Création de la personne
                sql = """
                    INSERT INTO person (
                        last_name, 
                        first_name) 
                    VALUES (%s,%s)
                """

                cursor.execute(
                    sql,
                    (
                        jury_member.last_name,
                        jury_member.first_name
                    )
                )

                id_person = cursor.lastrowid

                # Création du membre du jury
                sql = """
                    INSERT INTO jury_member (
                        is_president, 
                        id_person) 
                    VALUES (%s,%s)
                """

                cursor.execute(
                    sql,
                    (
                        jury_member.is_president,
                        id_person,
                    )
                )

                id_jury_member = cursor.lastrowid

                Dao.connection.commit()

                jury_member.id_jury_member = id_jury_member
                jury_member.id_person = id_person

                return id_jury_member

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la création du membre du jury : {error}")
                return None

    def read(self, id_jury_member: int) -> JuryMember | None:
        """Retourne le membre du jury correspondant à l'identifiant fourni
           ou None s'il n'a pu être trouvé"""

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    SELECT 
                        jury_member.id_jury_member,
                        jury_member.is_president,
                        person.id_person,
                        person.last_name,
                        person.first_name                         
                    FROM jury_member
                    JOIN person ON person.id_person = jury_member.id_person
                    WHERE jury_member.id_jury_member = %s
                """
                cursor.execute(sql, (id_jury_member,))
                record = cursor.fetchone()

                if record is not None:
                    return JuryMember(
                        id_jury_member=record['id_jury_member'],
                        is_president=record['is_president'],
                        id_person=record['id_person'],
                        last_name=record['last_name'],
                        first_name=record['first_name']
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture du membre du jury : {error}")

        return None

    def update(self, jury_member: JuryMember) -> bool:
        """Met à jour en BD l'entité JuryMember correspondant à jury_member, pour y correspondre
        :param jury_member: le membre du jury déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        if jury_member.id_jury_member is None or jury_member.id_person is None:
            return False

        with Dao.connection.cursor() as cursor:
            try:
                # Mise à jour des informations de la personne
                sql = """
                    UPDATE person
                    SET last_name = %s, 
                        first_name = %s
                    WHERE id_person = %s
                """

                cursor.execute(
                    sql,
                    (
                        jury_member.last_name,
                        jury_member.first_name,
                        jury_member.id_person
                    )
                )

                # Mise à jour des informations du membre du jury
                sql = """
                    UPDATE jury_member
                    SET is_president = %s
                    WHERE id_jury_member = %s
                """

                cursor.execute(
                    sql,
                    (
                        jury_member.is_president,
                        jury_member.id_jury_member
                    )
                )

                Dao.connection.commit()

                return True
            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la modification du membre du jury : {error}")
                return False

    def read_president(self) -> JuryMember | None:
        """Retourne le président du jury
           ou None s'il n'a pu être trouvé"""

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    SELECT 
                        jury_member.id_jury_member,
                        jury_member.is_president,
                        person.id_person,
                        person.last_name,
                        person.first_name                         
                    FROM jury_member
                    JOIN person ON person.id_person = jury_member.id_person
                    WHERE jury_member.is_president = TRUE
                """
                cursor.execute(sql)
                record = cursor.fetchone()

                if record is not None:
                    return JuryMember(
                        id_jury_member=record['id_jury_member'],
                        is_president=record['is_president'],
                        id_person=record['id_person'],
                        last_name=record['last_name'],
                        first_name=record['first_name']
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture du président : {error}")

        return None
