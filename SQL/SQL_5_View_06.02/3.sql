-- VIEW с условием: Создайте представление v_high_salary,
-- отображающее только тех сотрудников, у кого salary > 100000.
-- Затем сделайте SELECT из v_high_salary и убедитесь, что
-- вывелись только «высокие» зарплаты.

CREATE VIEW v_high_salary AS
SELECT *
FROM employees AS e
WHERE salary > 100000;

SELECT *
FROM v_high_salary;