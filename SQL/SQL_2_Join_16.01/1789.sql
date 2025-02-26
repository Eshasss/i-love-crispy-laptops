# Write your MySQL query statement below
SELECT e.employee_id,
       IFNULL(ee.department_id, e.department_id) AS department_id
FROM Employee AS e
LEFT JOIN Employee AS ee 
    ON e.employee_id = ee.employee_id AND ee.primary_flag = 'Y'
GROUP BY e.employee_id;
