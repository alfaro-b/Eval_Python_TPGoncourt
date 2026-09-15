# -*- coding: utf-8 -*-

"""
Classe Publisher
"""
from dataclasses import dataclass, field


@dataclass
class Publisher:
    """Représente l'éditeur d'un livre.
    name: nom de l'éditeur
    id_publisher: clé primaire de l'entité persistante, facultative avant enregistrement
    """
    name: str
    id_publisher: int | None = field(default=None)

    def __str__(self) -> str:
        return self.name
