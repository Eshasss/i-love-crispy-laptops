-- Создание VIEW для объединения таблиц: Создайте VIEW
-- (например, v_employee_info) на основе employees и
-- departments, выводя emp_name, salary, dept_name. Отберите
-- только сотрудников, у которых зарплата выше среднего в их
-- отделе (подумайте, можно ли использовать оконную функцию
-- прямо в CREATE VIEW)

CREATE VIEW v_employee_info AS
SELECT e.emp_name, e.salary,d.dept_name, AVG(e.salary)
FROM employees AS e
JOIN departments AS d  ON e.dept_id = d.dept_id
GROUP BY d.dept_id
HAVING  e.salary > AVG(e.salary);
