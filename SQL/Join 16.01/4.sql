--Напишите запрос, получающий информацию о названии альбома,
-- имени испонителя и общем количестве проданных копий альбома
SELECT a.title AS album_name, art.name AS art_name, SUM(i.quantity) AS sold
FROM album AS a
INNER JOIN artist AS art
    ON art.artist_id = a.artist_id
INNER JOIN track AS t
    ON a.album_id = t.album_id
INNER JOIN invoice_line AS i
    ON t.track_id = i.track_id
GROUP BY t.album_id;
