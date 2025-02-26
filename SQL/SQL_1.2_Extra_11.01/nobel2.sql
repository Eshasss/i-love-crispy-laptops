--1
SELECT COUNT(winner) FROM nobel;

--2
SELECT subject
FROM nobel
GROUP BY subject;

--3
SELECT COUNT(*)
FROM nobel
WHERE subject = 'physics';

--4
SELECT subject, COUNT(*) 
FROM nobel
GROUP BY subject

--5
SELECT subject, yr
FROM nobel
GROUP BY subject

--6
SELECT subject, COUNT(*)
FROM nobel
WHERE yr = 2000
GROUP BY subject

--7
SELECT subject, COUNT(DISTINCT winner)
FROM nobel
GROUP BY subject

--8 
SELECT subject, COUNT(DISTINCT yr)
FROM nobel
GROUP BY subject

--9 
SELECT yr
FROM nobel
WHERE subject = 'physics'
GROUP BY yr
HAVING COUNT(*) = 3
-- 10
SELECT winner
FROM nobel
GROUP BY winner
HAVING COUNT(*) > 1

--11

-- 12
SELECT yr, subject
FROM nobel 
GROUP BY yr, subject
HAVING COUNT(*) > 3
