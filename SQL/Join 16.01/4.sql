-- Напишите запрос, получающий информацию о названии альбома,
-- имени испонителя и общем количестве проданных копий альбома

SELECT a.title, ar.name
FROM album as a
INNER JOIN artist as ar
ON a.artist_id = ar.artist_id
INNER JOIN 