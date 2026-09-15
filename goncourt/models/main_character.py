# -*- coding: utf-8 -*-

"""
Classe MainCharacter
"""
from dataclasses import dataclass, field


@dataclass
class MainCharacter:
    """Représente un personnage principal d'un livre.
    name: nom du personnage
    id_book : identifiant du livre auquel appartient le personnage
    id_main_character: clé primaire de l'entité persistante, facultative avant enregistrement
    """
    name: str
    id_book: int
    id_main_character: int | None = field(default=None)

    def __str__(self) -> str:
        return self.name
