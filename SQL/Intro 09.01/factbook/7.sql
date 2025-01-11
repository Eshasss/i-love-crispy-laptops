-- 7. Выведите топ-10 стран по населению (facts_id - идентификатор
-- страны)
SELECT name, population
FROM facts
ORDER BY population DESC
LIMIT 10;