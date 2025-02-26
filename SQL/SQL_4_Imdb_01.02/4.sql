--Для каждого из актеров в пункте выше выведите: 
--максимальную, минимальную и среднюю (округленную до 2-х знаков после запятой) 
--оценки за фильмы с их участием, а также количество фильмов, в которых они снялись.
SELECT p.name, MAX(r.rating) AS max_rating,  MIN(r.rating) AS min_rating, ROUND(AVG(r.rating), 2) AS avg_rating, COUNT(t.title_id) AS film_count
FROM titles t
INNER JOIN crew AS c ON t.title_id = c.title_id
INNER JOIN people AS p ON c.person_id = p.person_id
INNER JOIN rating AS r ON t.title_id = r.title_id
WHERE p.name IN ('Tom Hanks', 'Julia Roberts', 'Natalie Portman')
GROUP BY p.name;