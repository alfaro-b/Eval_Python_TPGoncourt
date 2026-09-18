# -*- coding: utf-8 -*-

"""
Classe Dao[Publisher]
"""

from models.publisher import Publisher
from daos.dao import Dao
from dataclasses import dataclass


@dataclass
class PublisherDao(Dao[Publisher]):
    def read_all(self) -> list[Publisher]:
        """Retourne la liste de tous les éditeurs.

        :return: liste de tous les éditeurs
        """
        publishers: list[Publisher] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM publisher"
                cursor.execute(sql)
                records = cursor.fetchall()

                for record in records:
                    publisher = Publisher(
                        name=record['name'],
                        id_publisher=record['id_publisher']
                    )
                    publishers.append(publisher)
            except Exception as error:
                print(f"Erreur lors de la lecture des éditeurs {error}")

        return publishers

    def create(self, publisher: Publisher) -> int | None:
        """Crée un éditeur en BDD.

        :param publisher: éditeur à créer
        :return: identifiant de l'éditeur créé, ou None en cas d'échec
        """
        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    INSERT INTO publisher (name)
                    VALUES (%s)
                """

                cursor.execute(sql, (publisher.name,))

                id_publisher = cursor.lastrowid

                Dao.connection.commit()

                publisher.id_publisher = id_publisher

                return id_publisher

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la création de l'éditeur : {error}")
                return None

    def read(self, id_publisher: int) -> Publisher | None:
        """Retourne l'éditeur correspondant à l'identifiant fourni.

        :param id_publisher: identifiant de l'éditeur
        :return: éditeur trouvé, ou None s'il n'existe pas
        """

        with Dao.connection.cursor() as cursor:
            try:
                sql = """SELECT * 
                FROM publisher
                WHERE id_publisher=%s"""
                cursor.execute(sql, (id_publisher,))
                record = cursor.fetchone()

                if record is not None:
                    return Publisher(
                        name=record['name'],
                        id_publisher=record['id_publisher']
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture de l'éditeur : {error}")

        return None

    def update(self, publisher: Publisher) -> bool:
        """Met à jour un éditeur en BDD.

        :param publisher: éditeur contenant les nouvelles données
        :return: True si la mise à jour a été réalisée, False sinon
        """
        if publisher.id_publisher is None:
            return False

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    UPDATE publisher
                    SET name = %s
                    WHERE id_publisher = %s
                """

                cursor.execute(sql, (publisher.name, publisher.id_publisher))

                Dao.connection.commit()

                return True
            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la modification de l'éditeur : {error}")
                return False
