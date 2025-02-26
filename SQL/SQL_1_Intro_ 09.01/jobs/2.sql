-- 2. Напишите запрос, получающий процентную долю мужчин в
-- каждой сфере занятости (Major)
SELECT Major, (1 - ShareWomen) * 100 as ShareMen
FROM recent_grads;