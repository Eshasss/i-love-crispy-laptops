
-- 5. Напишите запрос, получающий катеоргии занятости, для которых
-- показатель женской занятости (из задания 1) находится в
-- промежутке от 3 до 5
SELECT major_category, SUM(ShareWomen) AS  ZanyatnostWomen
FROM recent_grads
GROUP BY major_category
HAVING SUM(ShareWomen) BETWEEN 3 AND 5;

