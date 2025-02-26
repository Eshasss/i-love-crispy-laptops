-- DENSE_RANK() по отделам: Сгруппируйте сотрудников по
-- отделам и упорядочьте внутри отдела по зарплате по убыванию.


SELECT DENSE_RANK() OVER (partition by e.dept_id ORDER BY e.salary DESC) AS dense_rank, *
FROM employees AS e
JOIN departments AS d ON e.dept_id = d.dept_id;