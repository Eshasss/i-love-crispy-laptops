-- Получите все фильмы, в которых играли Том Хэнкс (Tom Hanks), Джулия Робертс (Julia Roberts) или Натали Портман (Natalie Portman). Для каждого выведите имя актера, название фильма, год его выхода и оценку, отсортировав от лучших к худшим.
SELECT p.name, t.title, t.premiered, r.rating
FROM titles AS t
INNER JOIN crew AS c ON t.title_id = c.title_id
INNER JOIN people AS p ON c.person_id = p.person_id
INNER JOIN rating AS r ON t.title_id = r.title_id
WHERE p.name IN ('Tom Hanks', 'Julia Roberts', 'Natalie Portman')
ORDER BY r.rating DESC; 