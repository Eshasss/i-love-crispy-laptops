# Write your MySQL query statement below
SELECT e1.employee_id, e1.name, COUNT(e2.reports_to) AS reports_count, ROUND(AVG(e2.age), 0) AS average_age
FROM Employees AS e1
INNER JOIN Employees  AS e2
ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
HAVING COUNT(e2.reports_to) >= 1
ORDER BY e1.employee_id ASC;