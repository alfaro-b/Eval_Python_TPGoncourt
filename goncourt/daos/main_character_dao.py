# -*- coding: utf-8 -*-

"""
Classe Dao[MainCharacter]
"""

from models.main_character import MainCharacter
from daos.dao import Dao
from dataclasses import dataclass


@dataclass
class MainCharacterDao(Dao[MainCharacter]):
    def read_all(self) -> list[MainCharacter]:
        main_characters: list[MainCharacter] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM main_character"
                cursor.execute(sql)
                records = cursor.fetchall()

                for record in records:
                    main_character = MainCharacter(
                        id_main_character=record['id_main_character'],
                        name=record['name'],
                        id_book=record['id_book']
                    )
                    main_characters.append(main_character)
            except Exception as error:
                print(f"Erreur lors de la lecture des personnages principaux {error}")

        return main_characters

    def create(self, main_character: MainCharacter) -> int | None:
        """Crée en BD l'entité MainCharacter correspondant à main_character

        :param main_character: personnage principal à créer en BDD sous forme d'entité main_character
        :return: l'id de l'entité insérée en BDD
        """
        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    INSERT INTO main_character (name, id_book)
                    VALUES (%s,%s)
                """

                cursor.execute(sql, (main_character.name, main_character.id_book))

                id_main_character = cursor.lastrowid

                Dao.connection.commit()

                main_character.id_main_character = id_main_character

                return id_main_character

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la création du personnage principal : {error}")
                return None

    def read(self, id_main_character: int) -> MainCharacter | None:
        """Retourne le personnage principal correspondant à l'identifiant fourni
           ou None s'il n'a pu être trouvé"""

        with Dao.connection.cursor() as cursor:
            try:
                sql = """SELECT * 
                FROM main_character
                WHERE id_main_character=%s"""
                cursor.execute(sql, (id_main_character,))
                record = cursor.fetchone()

                if record is not None:
                    return MainCharacter(
                        id_main_character=record['id_main_character'],
                        name=record['name'],
                        id_book=record['id_book']
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture du personnage principal : {error}")

        return None

    def update(self, main_character: MainCharacter) -> bool:
        """Met à jour en BD l'entité MainCharacter correspondant à main_character, pour y correspondre
        :param main_character: le personnage principal déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        if main_character.id_main_character is None:
            return False

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    UPDATE main_character
                    SET name = %s, id_book = %s
                    WHERE id_main_character = %s
                """

                cursor.execute(sql, (main_character.name, main_character.id_book, main_character.id_main_character))

                Dao.connection.commit()

                return True
            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la modification du personnage principal : {error}")
                return False

    def read_by_book(self, id_book: int) -> list[MainCharacter]:
        """ Retourne les personnages principaux correspondant à un livre

        :param id_book: identifiant du livre
        :return: liste des personnages principaux
        """
        main_characters: list[MainCharacter] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM main_character WHERE id_book=%s"
                cursor.execute(sql, (id_book,))
                records = cursor.fetchall()

                for record in records:
                    main_character = MainCharacter(
                        id_main_character=record['id_main_character'],
                        name=record['name'],
                        id_book=record['id_book']
                    )
                    main_characters.append(main_character)
            except Exception as error:
                print(f"Erreur lors de la lecture des personnages principaux {error}")

        return main_characters
