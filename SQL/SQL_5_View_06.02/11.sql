-- Дополнительный вызов: обновление представления?
-- Попробуйте выполнить UPDATE или INSERT через созданное VIEW
-- и проверьте, даёт ли это результат или ошибку в SQLite

CREATE VIEW view11 AS
SELECT position
FROM employees;
INSERT INTO view11 VALUES ('MyPos');

-- cannot modify vvv because it is a view