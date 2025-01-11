-- 5. Напишите запрос, получающий новую колонку Population_%,
-- содержащую информацию о доле населения в городе
-- относительно населения всех городов представленных в таблице

SELECT name, 
    cast(population as float) / (SELECT SUM(population) FROM cities) AS "Population_%"
FROM cities;