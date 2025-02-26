-- Получите такие фильмы, где собралось сразу несколько актеров,
--  сыгравших в фильмах более чем 100 жанров. 
--  Для каждого выведите название фильма, год его выхода, 
-- --  оценку, жанры, количество подобных "разноплановых" актеров и их имена, 
-- --  отсортировав по количеству актеров2.



WITH ppl100 AS (
    SELECT p.person_id, p.name
    FROM film_genres AS fg
    JOIN titles AS t ON fg.title_id = t.title_id
    JOIN crew AS c ON c.title_id = t.title_id
    JOIN people AS p ON p.person_id = c.person_id
    GROUP BY p.person_id, p.name
    HAVING COUNT(fg.genre_id) > 100
),
flms AS (
    SELECT t.title_id, COUNT(ppl100.person_id) AS actor_count
    FROM titles AS t
    JOIN crew AS c ON c.title_id = t.title_id
    JOIN ppl100 ON ppl100.person_id = c.person_id
    GROUP BY t.title_id
    HAVING COUNT(ppl100.person_id) > 1
)
SELECT 
    t.title,
    t.premiered,
    r.rating,
    GROUP_CONCAT(DISTINCT gt.genre_name) AS genres,
    flms.actor_count AS actor_counts,
    GROUP_CONCAT(DISTINCT ppl100.name) AS actors
FROM flms
JOIN titles AS t ON flms.title_id = t.title_id
JOIN rating AS r ON t.title_id = r.title_id
JOIN film_genres AS fg ON t.title_id = fg.title_id
JOIN genre_types AS gt ON fg.genre_id = gt.id
JOIN crew AS c ON t.title_id = c.title_id
JOIN ppl100 ON ppl100.person_id = c.person_id
GROUP BY t.title, t.premiered, r.rating, flms.actor_count
ORDER BY flms.actor_count DESC;