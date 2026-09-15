# -*- coding: utf-8 -*-

"""
Classe Author
"""
from dataclasses import dataclass, field
from .person import Person


@dataclass
class Author(Person):
    """Auteur d'un ou plusieurs livres :
    id : clé primaire de l'entité persistante
    biography : biographie facultative de l'auteur
    """
    biography: str | None = field(default=None)
    id_author: int | None = field(default=None)

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, biographie :  {self.biography}"
