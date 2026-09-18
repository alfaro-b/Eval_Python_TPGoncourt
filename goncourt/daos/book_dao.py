# -*- coding: utf-8 -*-

"""
Classe Dao[Book]
"""

from models.book import Book
from daos.dao import Dao
from dataclasses import dataclass


@dataclass
class BookDao(Dao[Book]):
    def read_all(self) -> list[Book]:
        """Retourne la liste de tous les livres.

        :return:liste de tous les livres
        """
        books: list[Book] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = "SELECT * FROM book"
                cursor.execute(sql)
                records = cursor.fetchall()

                for record in records:
                    book = Book(
                        id_book=record['id_book'],
                        title=record['title'],
                        summary=record['summary'],
                        publication_date=record['publication_date'],
                        nbr_pages=record['nbr_pages'],
                        isbn=record['isbn'],
                        publisher_price=record['publisher_price'],
                        id_author=record['id_author'],
                        id_publisher=record['id_publisher']
                    )
                    books.append(book)
            except Exception as error:
                print(f"Erreur lors de la lecture des livres {error}")

        return books

    def create(self, book: Book) -> int | None:
        """Crée un livre en BDD.

        :param book: livre à créer
        :return: identifiant du livre créé, ou None en cas d'échec
        """
        with Dao.connection.cursor() as cursor:
            try:
                sql = """INSERT INTO book (
                    title, 
                    summary, 
                    publication_date, 
                    nbr_pages, 
                    isbn, 
                    publisher_price, 
                    id_author, 
                    id_publisher) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                """

                cursor.execute(
                    sql,
                    (
                        book.title,
                        book.summary,
                        book.publication_date,
                        book.nbr_pages,
                        book.isbn,
                        book.publisher_price,
                        book.id_author,
                        book.id_publisher
                    )
                )

                id_book = cursor.lastrowid

                Dao.connection.commit()

                book.id_book = id_book

                return id_book

            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la création du livre : {error}")
                return None

    def read(self, id_book: int) -> Book | None:
        """Retourne le livre correspondant à l'identifiant fourni.

        :param id_book: identifiant du livre
        :return: livre trouvé, ou None s'il n'existe pas
        """

        with Dao.connection.cursor() as cursor:
            try:
                sql = """SELECT * 
                FROM book
                WHERE id_book=%s"""
                cursor.execute(sql, (id_book,))
                record = cursor.fetchone()

                if record is not None:
                    return Book(
                        id_book=record['id_book'],
                        title=record['title'],
                        summary=record['summary'],
                        publication_date=record['publication_date'],
                        nbr_pages=record['nbr_pages'],
                        isbn=record['isbn'],
                        publisher_price=record['publisher_price'],
                        id_author=record['id_author'],
                        id_publisher=record['id_publisher'],
                    )

            except Exception as error:
                print(f"Erreur lors de la lecture du livre : {error}")

        return None

    def update(self, book: Book) -> bool:
        """Met à jour un livre en BDD.

        :param book: livre contenant les nouvelles données
        :return: True si la mise à jour a été réalisée, False sinon
        """
        if book.id_book is None:
            return False

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                    UPDATE book 
                    SET title = %s, 
                        summary = %s, 
                        publication_date = %s, 
                        nbr_pages = %s, 
                        isbn = %s, 
                        publisher_price = %s, 
                        id_author = %s, 
                        id_publisher = %s 
                    WHERE id_book = %s
                """

                cursor.execute(
                    sql,
                    (
                        book.title,
                        book.summary,
                        book.publication_date,
                        book.nbr_pages,
                        book.isbn,
                        book.publisher_price,
                        book.id_author,
                        book.id_publisher,
                        book.id_book
                    )
                )

                Dao.connection.commit()

                return True
            except Exception as error:
                Dao.connection.rollback()
                print(f"Erreur lors de la modification du livre : {error}")
                return False

    def read_by_selection(self, id_selection: int) -> list[Book]:
        """Retourne les livres appartenant à une sélection.

        :param id_selection: identifiant de la sélection
        :return: liste des livres appartenant à la sélection
        """
        books: list[Book] = []

        with Dao.connection.cursor() as cursor:
            try:
                sql = """
                SELECT book.* 
                FROM book
                JOIN belong ON book.id_book = belong.id_book
                WHERE belong.id_selection=%s
                """
                cursor.execute(sql, (id_selection,))
                records = cursor.fetchall()

                for record in records:
                    book = Book(
                        id_book=record['id_book'],
                        title=record['title'],
                        summary=record['summary'],
                        publication_date=record['publication_date'],
                        nbr_pages=record['nbr_pages'],
                        isbn=record['isbn'],
                        publisher_price=record['publisher_price'],
                        id_author=record['id_author'],
                        id_publisher=record['id_publisher']
                    )
                    books.append(book)
            except Exception as error:
                print(f"Erreur lors de la lecture des livres {error}")

        return books
