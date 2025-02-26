
--7
SELECT subject, COUNT(DISTINCT winner)
FROM nobel
GROUP BY subject