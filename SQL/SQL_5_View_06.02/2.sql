-- Добавление вычисляемого поля в VIEW: Создайте
-- представление, где помимо основных полей будет столбец
-- «годовая зарплата» = salary * 12. Покажите пример SELECT из
-- этого представления.


CREATE VIEW view2 AS
SELECT emp_id, emp_name, position, salary, dept_id, salary * 12 AS annual_salary
FROM employees;


SELECT *
FROM view2;