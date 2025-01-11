-- 3. Напишите запрос, получающий топ-20 столиц по населению
SELECT name, population
FROM cities
WHERE capital = 1
ORDER BY population DESC
LIMIT 20;