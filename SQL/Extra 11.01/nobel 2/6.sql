--6
SELECT subject, COUNT(*)
FROM nobel
WHERE yr = 2000
GROUP BY subject