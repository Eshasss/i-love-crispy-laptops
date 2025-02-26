"""
Modeling the db
"""

import sqlite3


from dataclasses import dataclass
from db.utils import get_script_from_file

@dataclass
class Book:
    """
    Class implementing task table logic
    """

    class BookObjects:
        """
        Proxy class for task table
        """

        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"books/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, int, str, int, int]]:
            """
            all
            """
            return self._template_query("all.sql")

        def create(self, name: str, author:str, year: int, \
                   edition: int, bookcase: int, bookshelf: int) -> None:
            """
            create
            """
            return self._template_query("create.sql", name, author, year, \
                                        edition, bookcase, bookshelf)

        def delete(self, book_id: int) -> None:
            """
            deletes
            """
            return self._template_query("del.sql", book_id)

        def get_place(self, bookcase_id: int, bookshelf: int) -> str:
            """
            get book by its positions
            """
            return self._template_query("get_place.sql", bookcase_id, bookshelf)

        def get_year(self, year: int) -> list[tuple[str, str]]:
            """
            books published in that year and its author
            """
            return self._template_query("get_year.sql", year)


        def get_author(self, author: int) -> list[tuple[str]]:
            """
            books that are published by that author
            """
            return self._template_query("get_author.sql", author)

    conn: sqlite3.Connection
    objects: BookObjects

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Book.BookObjects(self.conn)

@dataclass
class Visitor:
    """
    Class implementing visitors table logic
    """

    class VisitorObjects:
        """
        Proxy class for visitors table
        """

        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"visitors/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[str, str, str, int, str]]:
            """
            all
            """
            return self._template_query("all.sql")

        def create(self, name: str, surname: str, middle_name: str, \
                   library_card_id: int, adress: str) -> None:
            """
            create
            """
            return self._template_query("create.sql", name, surname, \
                                        middle_name, library_card_id, adress)

        def delete(self, visitor_id: int) -> None:
            """
            delete
            """
            return self._template_query("del.sql", visitor_id)

    conn: sqlite3.Connection
    objects: VisitorObjects

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Visitor.VisitorObjects(self.conn)

@dataclass
class Status:
    """
    Class implementing status table logic
    """

    class StatusObjects:
        """
        Proxy class for status table
        """

        conn: sqlite3.Connection

        def __init__(self, conn: sqlite3.Connection) -> None:
            self.conn = conn

        def _template_query(self, script: str, *args) -> list[tuple]:
            cursor = self.conn.cursor()
            script = get_script_from_file(f"status/{script}")
            res = cursor.execute(script, args)
            self.conn.commit()
            return res.fetchall()

        def all(self) -> list[tuple[int, int]]:
            """
            all
            """
            return self._template_query("all.sql")

        def create(self, book_id: int, visitor_id: int) -> None:
            """
            create
            """
            return self._template_query("create.sql", book_id, visitor_id)

        def delete(self, book_id: int) -> None:
            """
            delete
            """

            return self._template_query("del.sql", book_id)

        def get_books(self, card_id: int) -> list[tuple[str]]:
            """
            name the bookss somebody own by their card
            """
            return self._template_query("get_books.sql", card_id)

        def get_visit(self, name: str) -> list[tuple[str, int]]:
            """
            name who owns this book
            """
            return self._template_query("get_visit.sql", name)

    conn: sqlite3.Connection
    objects: StatusObjects

    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        cursor = self.conn.cursor()
        cursor.executescript(get_script_from_file("db_init.sql"))
        self.conn.commit()
        self.objects = Status.StatusObjects(self.conn)
