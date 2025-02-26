-- 1. Первые 10 комедий, вышедших не ранее 2019 года
SELECT t.title, t.premiered
FROM titles AS t
INNER JOIN film_genres AS fg  
ON t.title_id = fg.title_id
INNER JOIN genre_types AS gt ON fg.genre_id = gt.id
WHERE gt.genre_name = 'Comedy' AND t.premiered >= 2019
ORDER BY t.premiered ASC, t.title_id
LIMIT 10;
