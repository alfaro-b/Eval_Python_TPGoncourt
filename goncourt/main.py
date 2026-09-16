#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion du prix littéraire Goncourt
"""

from business.contest import Contest


def main() -> None:
    """Programme principal."""
    print("""--------- Bienvenue ---------""")

    contest = Contest()

    print('-' * 50)
    contest.display_selection(1)
    print('-' * 50)


if __name__ == '__main__':
    main()
