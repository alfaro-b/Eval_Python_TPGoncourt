# -*- coding: utf-8 -*-

"""
Classe Selection
"""
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Selection:
    """Représente une sélection du prix Goncourt.
    number: numéro de la sélection
    date : date de la sélection
    id_selection: clé primaire de l'entité persistante, facultative avant enregistrement
    """
    number: int
    date: date
    id_selection: int | None = field(default=None)

    def __str__(self) -> str:
        return (f"Prix Goncourt - Sélection {self.number}\n"
                f"Date : {self.date.strftime('%d/%m/%Y')}\n")

