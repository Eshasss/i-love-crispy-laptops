-- Сложный запрос + VIEW: Попробуйте объединить данные из
-- нескольких таблиц (например, employees, departments, projects
-- — если есть) в один запрос с оконной функцией, а затем сделайте
-- из него VIEW, чтобы упростить повторный доступ к этим
-- вычислениям

CREATE VIEW view12 AS
SELECT *, RANK() OVER (ORDER BY p.price DESC) AS pricing
FROM products AS p
JOIN orders AS o ON p.product_id = o.product_id
JOIN users AS u ON  o.user_id =  u.user_id
JOIN categories AS c ON p.cat_id = c.cat_id
GROUP BY p.product_id;

SELECT * FROM view12;
