-- 4. Напишите запрос, получающий последние 10 строк любых двух
-- колонок из таблицы facts
SELECT area_water, area_land
FROM facts
ORDER BY id DESC
LIMIT 10;