SELECT winner
FROM nobel
GROUP BY winner
HAVING COUNT(DISTINCT subject) > 1