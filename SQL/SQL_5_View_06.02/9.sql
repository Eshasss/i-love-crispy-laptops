-- Создание VIEW с оконной функцией: Создайте VIEW, в
-- котором каждая строка содержит emp_id, emp_name, и позицию
-- сотрудника (ROW_NUMBER()) в общем рейтинге по зарплате.
-- Убедитесь, что при SELECT * FROM <view_name> таблица
-- корректно отображает ранги

CREATE VIEW view9 AS
SELECT emp_id, emp_name, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
-- , salary Чтобы проверить
FROM employees;

SELECT * FROM view9;