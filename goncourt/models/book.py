# -*- coding: utf-8 -*-

"""
Classe Book
"""
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Book:
    """Représente un livre.
    title: titre du livre
    summary: résumé du livre
    publication_date: date de parution du livre
    nbr_pages: nombre de pages du livre
    isbn: code ISBN du livre
    publisher_price: prix éditeur du livre
    id_author: identifiant de l'auteur du livre
    id_publisher: identifiant de l'éditeur du livre
    id_book : clé primaire de l'entité persistante, facultative avant enregistrement
    """
    title: str
    summary: str
    publication_date: date
    nbr_pages: int
    isbn: str
    publisher_price: float
    id_author: int
    id_publisher: int
    id_book: int | None = field(default=None)

    def __str__(self) -> str:
        return (f"{self.title}\n "
                f"Résumé :  {self.summary}\n "
                f"Date de parution : {self.publication_date}\n"
                f"Nombre de pages : {self.nbr_pages}\n"
                f"ISBN : {self.isbn}\n"
                f"Prix : {self.publisher_price}\n"
                )
