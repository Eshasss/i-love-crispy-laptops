
SELECT *
FROM nobel
WHERE (subject = 'Medicine' and yr < 1910) OR (subject = 'Literature' and yr >= 2004);
