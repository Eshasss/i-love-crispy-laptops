
SELECT *
FROM nobel
WHERE subject NOT IN ('chemistry', 'medicine') AND yr = 1980;
