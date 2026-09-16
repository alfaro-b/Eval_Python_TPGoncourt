# -*- coding: utf-8 -*-

"""
Classe Contest
"""

from dataclasses import dataclass

from daos.book_dao import BookDao
from daos.author_dao import AuthorDao
from daos.publisher_dao import PublisherDao
from daos.main_character_dao import MainCharacterDao
from daos.selection_dao import SelectionDao


@dataclass
class Contest:
    """Couche métier de l'application de gestion du prix littéraire Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles.
    """

    def display_selection(self, selection_number: int):
        book_dao: BookDao = BookDao()
        author_dao: AuthorDao = AuthorDao()
        publisher_dao: PublisherDao = PublisherDao()
        main_character_dao: MainCharacterDao = MainCharacterDao()
        selection_dao: SelectionDao = SelectionDao()

        selection = selection_dao.read_by_number(selection_number)
        if selection is None:
            print("Selection inexistante")
            return

        books = book_dao.read_by_selection(selection.id_selection)

        print(selection)
        print('-' * 50)

        for book in books:
            author = author_dao.read(book.id_author)
            publisher = publisher_dao.read(book.id_publisher)
            characters = main_character_dao.read_by_book(book.id_book)

            print(book)
            print(f"Auteur : {author}")
            print(f"Editeur : {publisher}")

            if characters:
                print("Personnages principaux : ")
                for character in characters:
                    print(f"- {character}")
            else:
                print("Personnages principaux : non renseignés")

            print()
            print('-' * 30)
            print()
