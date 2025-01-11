-- 4. Напиште запрос, получающий все сферы занятости, где доля
-- женщин более половины от общего числа либо менее, но при
-- условии, что сфера занятости попадает в категорию Engineering
SELECT major, major_category, ShareWomen
FROM recent_grads
WHERE ShareWomen > 0.5 OR (ShareWomen <= 0.5 AND major_category = 'Engineering');
