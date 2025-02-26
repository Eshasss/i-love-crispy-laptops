-- -- Получите все фильмы определенного типа (сериал / фильм) и жанра, 
-- -- которые оценили бы больше 100 000 человек и чей рейтинг больше 8.
SELECT t.title, ft.film_type, gt.genre_name, r.rating, r.votes
FROM titles AS t
JOIN film_genres AS fg ON t.title_id = fg.title_id
JOIN genre_types AS gt ON fg.genre_id = gt.id
JOIN film_types AS ft ON t.type = ft.id
JOIN rating as r ON t.title_id = r.title_id
WHERE r.votes > 100000 AND r.rating > 8
GROUP BY ft.film_type, gt.genre_name
;
