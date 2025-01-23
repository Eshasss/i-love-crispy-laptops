# Write your MySQL query statement below
SELECT employee_id, department_id
FROM Employee 
GROUP BY employee_id
CASE THEN

WHERE primary_flag = 'Y'