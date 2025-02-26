-- посетитель у которого эта книга
SELECT v.name, v.library_card_id
FROM status as s
INNER JOIN visitors as v 
ON v.visitor_id = s.visitor_id
INNER JOIN books as b 
ON b.book_id = s.book_id
WHERE (b.name LIKE '%' || ? || '%') 