--8 
SELECT subject, COUNT(DISTINCT yr)
FROM nobel
GROUP BY subject