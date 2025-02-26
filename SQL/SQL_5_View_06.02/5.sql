-- Применение оконной функции ROW_NUMBER(): Напишите
-- запрос, который присваивает каждой записи о сотруднике
-- уникальный порядковый номер (по убыванию зарплаты).


SELECT emp_name, salary, ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num
FROM employees;
