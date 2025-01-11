SELECT continent, name
FROM world AS w
WHERE name = (
    SELECT MIN(name)
    FROM world
    WHERE continent = w.continent);
