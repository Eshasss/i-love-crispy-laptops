-- Для каждого клиента выведите суммарное количество средств на
-- его счетах. Полученные данные отсортируйте в порядке убывания
-- средств на счетах.
SELECT c.customer_id, c.first_name, c.last_name, SUM(i.total) AS balance
FROM customer as c
INNER JOIN invoice AS i
    ON c.customer_id = i.customer_id
GROUP BY c.customer_id
ORDER BY balance DESC;
