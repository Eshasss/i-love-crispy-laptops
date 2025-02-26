-- Агрегация с PARTITION BY: Для таблицы employees найдите,
-- какому отделу принадлежит каждый сотрудник и какова средняя
-- зарплата в этом отделе.

SELECT e.emp_name, d.dept_name, AVG(e.salary) OVER (PARTITION BY e.dept_id) AS avg_salary_in_dept
FROM employees AS e
JOIN departments AS d  ON e.dept_id = d.dept_id
;
