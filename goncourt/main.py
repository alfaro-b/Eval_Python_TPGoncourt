#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix littéraire Goncourt
"""
from random import choice

from business.contest import Contest
from daos.selection_dao import SelectionDao


def main() -> None:
    """Programme principal."""
    print("""--------- Bienvenue ---------""")

    print("Voici les sélections disponibles:")
    selection_dao: SelectionDao = SelectionDao()
    selections = selection_dao.read_all()
    for selection in selections:
        print(selection)

    choice = int(input("Saisissez le numéro de la sélection que vous souhaitez voir : "))

    contest = Contest()

    print('-' * 50)
    contest.display_selection(choice)
    print('-' * 50)


if __name__ == '__main__':
    main()
