-- SQLite

-- -- 2.1
SELECT name, population
FROM facts
LIMIT 10;

-- -- 2.2
SELECT capital, population
FROM cities
LIMIT 10;

-- 3. Напишите запрос, получающий топ-20 столиц по населению
SELECT name, population
FROM cities
WHERE capital = 1
ORDER BY population DESC
LIMIT 20;

-- 4. Напишите запрос, получающий последние 10 строк любых двух
-- колонок из таблицы facts
SELECT *
FROM facts
ORDER BY id DESC
LIMIT 10;

-- 5. Напишите запрос, получающий новую колонку Population_%,
-- содержащую информацию о доле населения в городе
-- относительно населения всех городов представленных в таблице

SELECT name, cast(population as float) / (SELECT SUM(population) FROM cities) AS "Population_%"
FROM cities;

-- 6. Напишите запрос, получающий все строки, содержащие NULL
--хотя бы в одной колонке
SELECT *
FROM facts
WHERE death_rate ISNULL OR area ISNULL OR area_land ISNULL OR area_water ISNULL OR population ISNULL OR population_growth ISNULL OR birth_rate ISNULL OR migration_rate ISNULL OR code ISNULL OR id ISNULL;

-- 7. Выведите топ-10 стран по населению (facts_id - идентификатор
-- страны)
SELECT *
FROM facts
ORDER BY population DESC
LIMIT 10;