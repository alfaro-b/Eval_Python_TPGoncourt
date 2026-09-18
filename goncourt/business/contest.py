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

    def display_selection(self, selection_number: int) -> None:
        book_dao: BookDao = BookDao()
        author_dao: AuthorDao = AuthorDao()
        publisher_dao: PublisherDao = PublisherDao()
        main_character_dao: MainCharacterDao = MainCharacterDao()
        selection_dao: SelectionDao = SelectionDao()

        selection = selection_dao.read_by_number(selection_number)

        if selection is None:
            print("Selection inexistante")
            return

        if selection.id_selection is None:
            print("Identifiant de sélection manquant")
            return

        books = book_dao.read_by_selection(selection.id_selection)

        print(selection)
        print('-' * 50)

        for book in books:
            author = author_dao.read(book.id_author)
            publisher = publisher_dao.read(book.id_publisher)

            characters = []
            if book.id_book is not None:
                characters = main_character_dao.read_by_book(book.id_book)

            print(book)
            print(f"Auteur : {author}")
            print(f"Éditeur : {publisher}")

            if characters:
                print("Personnages principaux : ")
                for character in characters:
                    print(f"- {character}")
            else:
                print("Personnages principaux : non renseignés")

            print()
            print('-' * 30)
            print()

    def indicate_selection_books(self):
        """Permet de renseigner les livres des deuxième et troisième sélections.

        Le président choisit la sélection à compléter, puis sélectionne les livres
        parmi ceux présents dans la sélection précédente.
        """
        selection_dao: SelectionDao = SelectionDao()
        book_dao: BookDao = BookDao()

        # Choix de la sélection à compléter
        try:
            selection_to_update = int(input("Choisissez la sélection à laquelle vous devez ajouter des livres : "))
        except ValueError:
            print("Veuillez choisir un numéro de sélection valide")
            return

        # Seules les deuxième et troisième sélections peuvent être renseignées
        if selection_to_update not in (2, 3):
            print("Vous pouvez uniquement renseigner les sélections 2 et 3.")
            return
        selection = selection_dao.read_by_number(selection_to_update)
        if selection is None:
            print("Selection inexistante")
            return

        # Récupération des livres de la sélection précédente
        previous_selection = selection_dao.read_by_number(selection_to_update - 1)
        if previous_selection is None:
            print("La sélection précédente n'existe pas.")
            return
        books = book_dao.read_by_selection(previous_selection.id_selection)

        print("Livres en compétition")
        for book in books:
            print(f"{book.id_book} - {book.title}")

        # Saisie des livres retenus pour la nouvelle sélection
        print(f"Choisissez les livres à ajouter à la sélection {selection.number}")
        books_choosed = input("Saisissez les numéros des livres séparés par / :")
        id_books = books_choosed.split("/")

        # Vérification que les livres choisis font bien partie de la sélection précédente
        try:
            for id_book in id_books:
                id_book = int(id_book)

                book_found = False

                for book in books:
                    if book.id_book == id_book:
                        book_found = True
                        break

                if not book_found:
                    print(f"Le livre {id_book} ne fait pas partie "
                          f"de la sélection précédente {previous_selection.number}.")
                    return

                selection_dao.add_book(selection.id_selection, id_book)

        except ValueError:
            print("Les identifiants des livres doivent être des nombres.")
            return

        # Affichage de la nouvelle sélection
        print("-" * 30)
        print("Voici maintenant les livres en compétitions :")
        print(selection)
        print("-" * 30)

        books_added = book_dao.read_by_selection(selection.id_selection)
        for book in books_added:
            print(book.title)

    def add_final_vote(self):
        """Permet au président d'ajouter le nombre de votes à un livre de la sélection 3."""
        selection_dao: SelectionDao = SelectionDao()
        book_dao: BookDao = BookDao()

        # Affichage de la liste des livres de la sélection 3
        selection = selection_dao.read_by_number(3)

        if selection is None:
            print("La sélection 3 n'existe pas.")
            return

        books_selection3 = book_dao.read_by_selection(selection.id_selection)

        print("-" * 30)
        print("Livres en compétitions - Sélection 3 : ")
        for book in books_selection3:
            votes = selection_dao.read_book_votes(selection.id_selection, book.id_book)

            if votes is None:
                print(f"{book.id_book} - {book.title} - Votes : non renseignés")
            else:
                print(f"{book.id_book} - {book.title} - Votes : {votes}")

        other_book: str = "oui"
        while other_book in ("oui", "o"):

            # Choix du livre
            print("-" * 30)
            print("Pour quel livre, vous souhaitez ajouter le nombre de votes? ")
            try:
                book_choosed_id = int(input("Saisissez le numéro du livre : "))
            except ValueError:
                print("Les identifiants des livres doivent être des nombres.")
                continue

            # Vérification que les livres choisis font bien partie de la sélection 3
            book_found = False

            for book in books_selection3:
                if book.id_book == book_choosed_id:
                    book_found = True
                    break

            if not book_found:
                print(f"Le livre {book_choosed_id} ne fait pas partie de la sélection 3.")
                continue

            # Saisie du nombre de votes pour le livre choisi
            book_choosed = book_dao.read(book_choosed_id)
            print("-" * 30)
            print(f"Pour le livre '{book_choosed.title}'")
            try:
                votes_nbr = int(input("Saisissez le nombre de votes "))
            except ValueError:
                print("Le nombre de votes doit être un nombre.")
                continue
            if votes_nbr < 0:
                print("Le nombre de votes ne peut être négatif.")
                continue

            selection_dao.add_votes(selection.id_selection, book_choosed_id, votes_nbr)

            # Réaffichage de la liste après ajout pour vérification
            books_selection3 = book_dao.read_by_selection(selection.id_selection)

            print("-" * 30)
            print("Livres en compétitions - Sélection 3 : ")
            for book in books_selection3:
                votes = selection_dao.read_book_votes(selection.id_selection, book.id_book)

                if votes is None:
                    print(f"{book.id_book} - {book.title} - Votes : non renseignés")
                else:
                    print(f"{book.id_book} - {book.title} - Votes : {votes}")

            other_book = input("Voulez-vous saisir un autre vote? Saisissez oui ou non. ").lower()

    def display_winner(self) -> None:
        """Détermine et affiche le livre ayant obtenu le plus de votes"""

        selection_dao: SelectionDao = SelectionDao()
        book_dao: BookDao = BookDao()
        author_dao: AuthorDao = AuthorDao()
        publisher_dao: PublisherDao = PublisherDao()
        main_character_dao: MainCharacterDao = MainCharacterDao()

        # Récupération des livres de la sélection 3
        selection = selection_dao.read_by_number(3)

        if selection is None:
            print("La sélection 3 n'existe pas.")
            return

        books_selection3 = book_dao.read_by_selection(selection.id_selection)

        # Détermination du gagnant
        winner = None
        max_votes = 0

        for book in books_selection3:
            votes = selection_dao.read_book_votes(selection.id_selection, book.id_book)

            if votes is None:
                continue

            if votes > max_votes:
                max_votes = votes
                winner = book

        # Affichage du gagnant
        if winner is None:
            print("Aucun vote n'a encore été renseigné.")
            return

        print("-" * 30)
        print(f"{selection}")
        print("-" * 30)
        print(f"Le livre '{winner.title}' est le gagnant avec {max_votes} votes.")
        print("-" * 30)

        author = author_dao.read(winner.id_author)
        publisher = publisher_dao.read(winner.id_publisher)
        characters = main_character_dao.read_by_book(winner.id_book)

        print(winner)
        print(f"Auteur : {author}")
        print(f"Editeur : {publisher}")

        if characters:
            print("Personnages principaux : ")
            for character in characters:
                print(f"- {character}")
        else:
            print("Personnages principaux : non renseignés")
        print("-" * 30)
