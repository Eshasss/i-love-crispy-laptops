-- 3. Напишите запрос, получающий топ-10 сфер занятости по доли
-- занятости женщин в этой сфере при условии что женщин не более
-- 0.8 и не менее 0.5 от общего числа
SELECT major, ShareWomen
FROM recent_grads
WHERE ShareWomen BETWEEN 0.5 AND 0.8
ORDER BY ShareWomen DESC
LIMIT 10;