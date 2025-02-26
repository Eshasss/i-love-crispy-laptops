-- Получите все фильмы, в которых играл Том Хэнкс (Tom Hanks). Для каждого выведите название и год его выхода, отсортировав от новых к старым.
SELECT t.title, t.premiered
FROM titles AS t
JOIN crew AS c ON t.title_id = c.title_id
JOIN people AS p ON c.person_id = p.person_id
WHERE p.name = 'Tom Hanks'
ORDER BY t.premiered DESC;