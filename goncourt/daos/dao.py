# -*- coding: utf-8 -*-

"""
Classe abstraite générique Dao[T], dont héritent les classes de DAO de chaque entité
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar
import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

db_host: str = os.environ["DB_HOST"]
db_user: str = os.environ["DB_USER"]
db_password: str = os.environ["DB_PASSWORD"]
db_name: str = os.environ["DB_NAME"]


@dataclass
class Dao[T](ABC):
    connection: ClassVar[pymysql.Connection[pymysql.cursors.DictCursor]] = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    @abstractmethod
    def create(self, obj: T) -> int | None:
        """Crée l'entité en BD correspondant à l'objet obj

        :param obj: à créer sous forme d'entité en BDD
        :return: l'id de l'entité insérée en BDD
        """
        ...

    @abstractmethod
    def read(self, id_entity: int) -> T | None:
        """Retourne l'objet correspondant à l'identifiant fourni,
           ou None s'il n'a pu être trouvé"""
        ...

    @abstractmethod
    def update(self, obj: T) -> bool:
        """Met à jour en BDD l'entité correspondant à obj, pour y correspondre

        :param obj: objet déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...

    @abstractmethod
    def read_all(self) -> list[T]:
        """Retourne tous les objets correspondant à l'entité
        ou une liste vide si aucun objet n'est trouvé."""
        ...
