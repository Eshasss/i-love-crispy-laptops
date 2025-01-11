--9 
SELECT yr
FROM nobel
WHERE subject = 'physics'
GROUP BY yr
HAVING COUNT(*) = 3