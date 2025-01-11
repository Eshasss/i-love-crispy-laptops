-- 7. Выведите топ-10 стран по населению (facts_id - идентификатор
-- страны)
SELECT name, population
FROM facts
WHERE facts.id IN (SELECT DISTINCT facts_id FROM cities)
ORDER BY population DESC
LIMIT 10;