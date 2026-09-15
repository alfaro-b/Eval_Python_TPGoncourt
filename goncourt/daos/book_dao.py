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
        """Crée en BD l'entité Book correspondant à book

        :param book: livre à créer en BDD sous forme d'entité book
        :return: l'id de l'entité insérée en BDD
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
        """Retourne le livre correspondant à l'identifiant fourni
           ou None s'il n'a pu être trouvé"""

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
        """Met à jour en BD l'entité Book correspondant à book, pour y correspondre
        :param book: le livre déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
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
