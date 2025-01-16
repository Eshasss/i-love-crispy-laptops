-- Напишите запрос, возвращающий для каждой страны следующие
-- значения: название страны, население страны, городское
-- население страны и процентное соотношение городского
-- населения к общему

SELECT f1.name, f1.population AS country_population, SUM(f2.population) AS city_population, cast(SUM(f2.population) as FLOAT)/cast(f1.population as FLOAT) * 100 AS city_to_country
FROM facts AS f1
INNER JOIN cities as f2
    ON f1.id = f2.facts_id
GROUP BY f1.name