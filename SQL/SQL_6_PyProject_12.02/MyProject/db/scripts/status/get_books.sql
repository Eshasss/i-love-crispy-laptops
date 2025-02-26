-- все книги одного посетителя по его карточке
SELECT b.name
FROM status as s
INNER JOIN visitors as v 
ON v.visitor_id = s.visitor_id
INNER JOIN books as b 
ON b.book_id = s.book_id
WHERE v.library_card_id = ?