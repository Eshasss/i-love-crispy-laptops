-- RANK() и одинаковая зарплата: Покажите, как RANK()
-- присваивает места сотрудникам, если у нескольких человек
-- зарплата совпадает.

SELECT emp_name, salary, RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees
ORDER BY salary_rank ASC;

-- Таковых нет...