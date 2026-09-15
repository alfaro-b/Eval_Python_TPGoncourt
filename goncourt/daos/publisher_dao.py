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
        """Crée en BD l'entité Publisher correspondant à publisher

        :param publisher: éditeur à créer en BDD sous forme d'entité publisher
        :return: l'id de l'entité insérée en BDD
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
        """Retourne l'éditeur correspondant à l'identifiant fourni
           ou None s'il n'a pu être trouvé"""

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
        """Met à jour en BD l'entité Publisher correspondant à publisher, pour y correspondre
        :param publisher: éditeur déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
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
