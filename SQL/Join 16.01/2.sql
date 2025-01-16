-- Напишите запрос, возвращающий каждой страны название,
-- количество городов в этой стране, столицу этой страны, население
-- столицы и процент населения столицы от общего населения
SELECT f1.name, f1.population AS country_population, COUNT(f2.name) AS cities_amount, f2.population AS capital_population, cast(SUM(f2.population) as FLOAT)/cast(f1.population as FLOAT) * 100 AS capital_to_country
FROM facts AS f1
INNER JOIN cities as f2
    ON f1.id = f2.facts_id
GROUP BY f1.name
HAVING f2.capital = 1s