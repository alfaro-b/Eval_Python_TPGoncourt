# -*- coding: utf-8 -*-

"""
Classe Dao[Selection]
"""

from models.selection import Selection
from daos.dao import Dao
from dataclasses import dataclass


@dataclass
class SelectionDao(Dao[Selection]):
    def read_all(self) -> list[Selection]:
        selections: list[Selection] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM selection"
                cursor.execute(sql)
                records = cursor.fetchall()

                for record in records:
                    selection = Selection(
                        id_selection=record['id_selection'],
                        number=record['number'],
                        date=record['date_']
                    )
                    selections.append(selection)
            except Exception as error:
                print(f"Erreur lors de la lecture des sélections {error}")

        return selections

    def create(self, selection: Selection) -> int | None:
        """Crée en BD l'entité Selection correspondant à selection

        :param selection: sélection à créer en BDD sous forme d'entité selection
        :return: l'id de l'entité insérée en BDD
        """
        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    INSERT INTO selection (number, date_)
                    VALUES (%s,%s)
                """

                cursor.execute(sql, (selection.number, selection.date))

                id_selection = cursor.lastrowid

                Dao.connection.commit()

                selection.id_selection = id_selection

                return id_selection

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la création de la sélection : {error}")
                return None

    def read(self, id_selection: int) -> Selection | None:
        """Retourne la sélection correspondante à l'identifiant fourni
           ou None s'il n'a pu être trouvé"""

        with Dao.connection.cursor() as cursor:
            try:
                sql = """SELECT * 
                FROM selection
                WHERE id_selection=%s"""
                cursor.execute(sql, (id_selection,))
                record = cursor.fetchone()

                if record is not None:
                    return Selection(
                        id_selection=record['id_selection'],
                        number=record['number'],
                        date=record['date_']
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture de la sélection : {error}")

        return None

    def update(self, selection: Selection) -> bool:
        """Met à jour en BD l'entité Selection correspondant à selection, pour y correspondre
        :param selection: la sélection déjà mise à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        if selection.id_selection is None:
            return False

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    UPDATE selection
                    SET number = %s, date_ = %s
                    WHERE id_selection = %s
                """

                cursor.execute(sql, (selection.number, selection.date, selection.id_selection))

                Dao.connection.commit()

                return True
            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la modification de la sélection : {error}")
                return False

    def read_by_number(self, number: int) -> Selection | None:
        """Retourne la sélection correspondante au numéro fourni
           ou None s'il n'a pu être trouvé"""

        with Dao.connection.cursor() as cursor:
            try:
                sql = """SELECT * 
                FROM selection
                WHERE number=%s"""
                cursor.execute(sql, (number,))
                record = cursor.fetchone()

                if record is not None:
                    return Selection(
                        id_selection=record['id_selection'],
                        number=record['number'],
                        date=record['date_']
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture de la sélection : {error}")

        return None

    def add_book(self, id_selection: int, id_book: int) -> bool:
        """Ajoute un livre à une sélection

        :param id_selection: identifiant de la sélection
        :param id_book: identifiant du livre
        :return: True si l'ajout a pu être réalisé
        """

        if id_selection is None or id_book is None:
            return False

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    INSERT INTO belong (id_selection, id_book)
                    VALUES (%s,%s)
                """
                cursor.execute(sql, (id_selection, id_book))

                Dao.connection.commit()

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de l'ajout du livre à la sélection : {error}")
                return False

        return True

    def add_votes(self, id_selection: int, id_book: int, votes_nbr: int) -> bool:
        """Ajoute le nombre de votes à un livre de la sélection

        :param votes_nbr: nombre de votes
        :param id_selection: identifiant de la sélection
        :param id_book: identifiant du livre
        :return: True si l'ajout a pu être réalisé
        """

        if id_selection is None or id_book is None:
            return False

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    UPDATE belong
                    SET votes_number = %s
                    WHERE id_selection = %s AND id_book = %s
                """
                cursor.execute(sql, (votes_nbr, id_selection, id_book))

                Dao.connection.commit()

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de l'ajout du nombre de votes : {error}")
                return False

        return True
