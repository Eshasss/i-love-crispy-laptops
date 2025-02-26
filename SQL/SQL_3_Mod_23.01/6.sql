CREATE TABLE products_copy (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price FLOAT);

INSERT INTO products_copy
   SELECT * FROM products;

DROP TABLE products;

ALTER TABLE products_copy RENAME TO products;
