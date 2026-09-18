# -*- coding: utf-8 -*-

"""
Classe Dao[Author]
"""
from models.author import Author
from daos.dao import Dao
from dataclasses import dataclass


@dataclass
class AuthorDao(Dao[Author]):
    def read_all(self) -> list[Author]:
        """Retourne la liste de tous les auteurs.

        :return: la liste de tous les auteurs
        """
        authors: list[Author] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    SELECT 
                        author.id_author,
                        author.biography,
                        person.id_person,
                        person.last_name,
                        person.first_name                         
                    FROM author
                    JOIN person ON person.id_person = author.id_person
                """
                cursor.execute(sql)
                records = cursor.fetchall()

                for record in records:
                    author = Author(
                        id_author=record['id_author'],
                        biography=record['biography'],
                        id_person=record['id_person'],
                        last_name=record['last_name'],
                        first_name=record['first_name']
                    )
                    authors.append(author)
            except Exception as error:
                print(f"Erreur lors de la lecture des auteurs {error}")

        return authors

    def create(self, author: Author) -> int | None:
        """Crée un auteur en BDD.

        :param author: auteur à créer
        :return: identifiant de l'auteur créé, ou None en cas d'échec
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
                        author.last_name,
                        author.first_name
                    )
                )

                id_person = cursor.lastrowid

                # Création de l'auteur
                sql = """
                    INSERT INTO author (
                        biography, 
                        id_person) 
                    VALUES (%s,%s)
                """

                cursor.execute(
                    sql,
                    (
                        author.biography,
                        id_person,
                    )
                )

                id_author = cursor.lastrowid

                Dao.connection.commit()

                author.id_author = id_author
                author.id_person = id_person

                return id_author

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la création de l'auteur : {error}")
                return None

    def read(self, id_author: int) -> Author | None:
        """Retourne l'auteur correspondant à l'identifiant fourni.

        :param id_author: identifiant de l'auteur
        :return: auteur trouvé, ou None s'il n'existe pas
        """

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    SELECT 
                        author.id_author,
                        author.biography,
                        person.id_person,
                        person.last_name,
                        person.first_name                         
                    FROM author
                    JOIN person ON person.id_person = author.id_person
                    WHERE author.id_author = %s
                """
                cursor.execute(sql, (id_author,))
                record = cursor.fetchone()

                if record is not None:
                    return Author(
                        id_author=record['id_author'],
                        biography=record['biography'],
                        id_person=record['id_person'],
                        last_name=record['last_name'],
                        first_name=record['first_name']
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture de l'auteur : {error}")

        return None

    def update(self, author: Author) -> bool:
        """Met à jour un auteur en BDD.

        :param author: auteur contenant les nouvelles données
        :return: True si la mise à jour a été réalisée, False sinon
        """
        if author.id_author is None or author.id_person is None:
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
                        author.last_name,
                        author.first_name,
                        author.id_person
                    )
                )

                # Mise à jour des informations de l'auteur
                sql = """
                    UPDATE author
                    SET biography = %s
                    WHERE id_author = %s
                """

                cursor.execute(
                    sql,
                    (
                        author.biography,
                        author.id_author
                    )
                )

                Dao.connection.commit()

                return True
            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la modification de l'auteur : {error}")
                return False
