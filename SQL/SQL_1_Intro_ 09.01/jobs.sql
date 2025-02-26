-- SQLite

-- 1. Напишите запрос, получающий все категории занятости
-- (Major_category), где сумма по всем сферам долей занятости
-- женщин более 5
SELECT Major_category, Sum(ShareWomen)
FROM 
    recent_grads
GROUP BY 
    Major_category
HAVING 
    SUM(ShareWomen) > 5;

-- 2. Напишите запрос, получающий процентную долю мужчин в
-- каждой сфере занятости (Major)
SELECT Major, (1 - ShareWomen) * 100 as ShareMen
FROM recent_grads;

-- 3. Напишите запрос, получающий топ-10 сфер занятости по доли
-- занятости женщин в этой сфере при условии что женщин не более
-- 0.8 и не менее 0.5 от общего числа
SELECT major, ShareWomen
FROM recent_grads
WHERE ShareWomen BETWEEN 0.5 AND 0.8
ORDER BY ShareWomen DESC
LIMIT 10;


-- 4. Напиште запрос, получающий все сферы занятости, где доля
-- женщин более половины от общего числа либо менее, но при
-- условии, что сфера занятости попадает в категорию Engineering
SELECT major, major_category, ShareWomen
FROM recent_grads
WHERE ShareWomen > 0.5 OR (ShareWomen <= 0.5 AND major_category = 'Engineering');


-- 5. Напишите запрос, получающий катеоргии занятости, для которых
-- показатель женской занятости (из задания 1) находится в
-- промежутке от 3 до 5
SELECT major_category, SUM(ShareWomen) AS  ZanyatnostWomen
FROM recent_grads
GROUP BY major_category
HAVING SUM(ShareWomen) BETWEEN 3 AND 5;

