-- Сравнение зарплаты с предыдущей строкой (LAG): Напишите
-- запрос, который для каждого сотрудника показывает его salary и
-- «предыдущую» зарплату — так вы сможете сравнить.


SELECT emp_id, salary,
    LAG(salary) OVER (ORDER BY emp_id) AS prev_salary
FROM employees;
