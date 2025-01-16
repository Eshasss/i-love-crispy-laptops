-- Напишите запрос, получающие следующие колонки из
-- объединения таблиц: invoice_id=1, track_id, track_name,
-- media_type_name, quantity и unit_price

SELECT 
FROM track AS t1
FULL JOIN invoice_line AS t2
ON t1.key = t2.key;
