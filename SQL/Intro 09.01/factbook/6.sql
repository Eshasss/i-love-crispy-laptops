-- 6. Напишите запрос, получающий все строки, содержащие NULL
--хотя бы в одной колонке
SELECT *
FROM facts
WHERE death_rate ISNULL OR area ISNULL OR area_land ISNULL OR area_water ISNULL OR population ISNULL OR population_growth ISNULL OR birth_rate ISNULL OR migration_rate ISNULL OR code ISNULL OR id ISNULL;
