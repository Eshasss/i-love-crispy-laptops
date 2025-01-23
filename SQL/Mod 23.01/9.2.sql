ALTER TABLE products
FOREIGN KEY (cat_id)
REFERENCES categories(cat_id);
