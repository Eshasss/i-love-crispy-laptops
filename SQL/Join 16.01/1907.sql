SELECT
    'Low Salary' AS category,
    COUNT(a.income) AS accounts_count
FROM
    Accounts AS a
RIGHT JOIN
    (SELECT 'Low Salary' AS category) acc ON a.income < 20000
GROUP BY
    acc.category
UNION
SELECT
    'Average Salary' AS category,
    COUNT(a.income) AS accounts_count
FROM
    Accounts AS a
RIGHT JOIN
    (SELECT 'Average Salary' AS category) acc ON a.income BETWEEN 20000 AND 50000
GROUP BY
    acc.category
UNION
SELECT
    'High Salary' AS category,
    COUNT(a.income) AS accounts_count
FROM
    Accounts AS a
RIGHT JOIN
    (SELECT 'High Salary' AS category) acc ON a.income > 50000
GROUP BY
    acc.category;
