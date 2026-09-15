# -*- coding: utf-8 -*-

"""
Classe JuryMember
"""
from dataclasses import dataclass, field
from .person import Person


@dataclass
class JuryMember(Person):
    """Membre du jury :
    id              : clé primaire de l'entité persistante
    is_president     : boolean
    """
    is_president: bool = field(default=None, init=False)

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, président :  {self.is_president}"
