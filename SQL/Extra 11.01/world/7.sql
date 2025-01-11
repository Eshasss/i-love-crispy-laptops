SELECT continent, name, area
FROM world AS w
WHERE area = (
    SELECT MAX(area)
    FROM world
    WHERE continent = w.continent
)
ORDER BY name;
