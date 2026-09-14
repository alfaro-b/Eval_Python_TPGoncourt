# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Author et Jury_member
"""

from abc import ABC
from dataclasses import dataclass, field


@dataclass
class Person(ABC):
    """Personne liée au concours : auteur ou membre du jury."""
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
