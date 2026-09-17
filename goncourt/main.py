#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix littéraire Goncourt
"""

from business.contest import Contest
from daos.selection_dao import SelectionDao


def main() -> None:

    """Programme principal."""

    contest = Contest()

    while True:
        print("""--------- Bienvenue ---------""")

        print("1- Consulter les sélections\n"
              "2- Espace président\n"
              "3- Quitter\n")

        user_choice = input("Votre choix : \n")

        # -------------------------
        # TOUT UTILISATEUR
        # -------------------------

        if user_choice == "1":

            print("Voici les sélections disponibles: \n")
            selection_dao: SelectionDao = SelectionDao()
            selections = selection_dao.read_all()
            for selection in selections:
                print(selection)

            selection_choosed = int(input("Saisissez le numéro de la sélection que vous souhaitez voir : "))

            print('-' * 50)
            contest.display_selection(selection_choosed)
            print('-' * 50)

        # -------------------------
        # PRESIDENT
        # -------------------------

        elif user_choice == "2":
            while True:
                print('-' * 50)
                print("Que souhaitez-vous faire ?\n")
                print("1- Définier les livres de la 2ème et 3ème sélection\n"
                      "2- Saisir les votes du dernier tour de scrutin pour les livres de la sélection 3\n"
                      "3- Quitter\n")

                president_choice = input("Votre choix : \n")

                if president_choice == "1":
                    # Ajout de livres à la sélection 2 ou 3
                    contest.indicate_selection_books()

                elif president_choice == "2":
                    # Ajout du nombre de votes à un livre de la sélection 3
                    contest.add_final_vote()

                elif president_choice == "3":
                    print("Au revoir")
                    break

                else:
                    print("Le choix n'est pas valide")

        # -------------------------
        # QUITTER
        # -------------------------

        elif user_choice == "3":
            print("Au revoir.")
            break

        else:
            print("Choix invalide.")


if __name__ == '__main__':
    main()
