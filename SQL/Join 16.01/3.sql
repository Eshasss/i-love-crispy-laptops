-- Напишите запрос, получающие следующие колонки из
-- объединения таблиц: invoice_id=1, track_id, track_name,
-- media_type_name, quantity и unit_price

SELECT i1.invoice_id, i2.track_id, t.name AS track_name, m.name AS media_type_name, i2.quantity, t.unit_price
FROM invoice AS i1
INNER JOIN invoice_line AS i2
ON i1.invoice_id = i2.invoice_id
INNER JOIN track AS t
ON i2.track_id = t.track_id
INNER JOIN media_type AS m
ON t.media_type_id = m.media_type_id
WHERE i2.invoice_id = 1;
