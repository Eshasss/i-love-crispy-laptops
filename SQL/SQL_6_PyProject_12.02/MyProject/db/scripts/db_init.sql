CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER,
    edition VARCHAR,
    bookcase_id INTEGER,
    bookshelf_id INTEGER
);

CREATE TABLE IF NOT EXISTS visitors (
    visitor_id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    surname VARCHAR,
    middle_name VARCHAR,
    library_card_id INTEGER,
    adress VARCHAR
);

CREATE TABLE IF NOT EXISTS status (
    status_id INTEGER PRIMARY KEY,
    book_id INTEGER,
    visitor_id INTEGER
);
