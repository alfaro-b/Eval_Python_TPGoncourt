#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix littéraire Goncourt
"""

from business.contest import Contest
from daos.selection_dao import SelectionDao


def main() -> None:
    """Programme principal."""
    print("""--------- Bienvenue ---------""")

    # Pour le président, ajout de livres à la sélection 2 ou 3
    contest = Contest()
    contest.indicate_selection_books()

    # Pour le président, ajout du nombre de votes à un livre de la sélection 3
    contest.add_final_vote()

    # # Pour tout utilisateur, affichage des livres en compétition
    print("Voici les sélections disponibles:")
    selection_dao: SelectionDao = SelectionDao()
    selections = selection_dao.read_all()
    for selection in selections:
        print(selection)

    choice = int(input("Saisissez le numéro de la sélection que vous souhaitez voir : "))

    print('-' * 50)
    contest.display_selection(choice)
    print('-' * 50)


if __name__ == '__main__':
    main()
