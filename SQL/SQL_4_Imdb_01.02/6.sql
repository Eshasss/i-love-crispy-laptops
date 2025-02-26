-- Получите топ-10 фильмов по рейтингу, где ровно 2 жанра и 100 000+ оценок1.
SELECT  t.title, t.premiered, r.rating, r.votes,GROUP_CONCAT(gt.genre_name) AS genres
FROM titles AS t
JOIN film_genres AS fg ON t.title_id = fg.title_id
JOIN genre_types AS gt ON fg.genre_id = gt.id
JOIN rating AS r ON t.title_id = r.title_id
GROUP BY t.title_id, t.title
HAVING COUNT(DISTINCT gt.genre_name) = 2 AND r.votes > 100000
ORDER BY r.rating DESC
LIMIT 10;

