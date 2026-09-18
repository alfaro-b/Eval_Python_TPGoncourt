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
        """Retourne la liste de tous les personnages principaux.

        :return:liste de tous les personnages principaux
        """
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
        """Crée un personnage principal en BDD.

        :param main_character: personnage principal à créer
        :return: identifiant du personnage créé, ou None en cas d'échec
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
        """Retourne le personnage principal correspondant à l'identifiant fourni.

        :param id_main_character: identifiant du personnage principal
        :return: personnage principal trouvé, ou None s'il n'existe pas
        """

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
        """Met à jour un personnage principal en BDD.

        :param main_character: personnage principal contenant les nouvelles données
        :return: True si la mise à jour a été réalisée, False sinon
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
        """Retourne les personnages principaux associés à un livre.

        :param id_book: identifiant du livre
        :return: liste des personnages principaux associés au livre
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
