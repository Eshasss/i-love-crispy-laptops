-- 1. Напишите запрос, получающий все категории занятости
-- (Major_category), где сумма по всем сферам долей занятости
-- женщин более 5
SELECT Major_category, Sum(ShareWomen)
FROM recent_grads
GROUP BY Major_category
HAVING SUM(ShareWomen) > 5;