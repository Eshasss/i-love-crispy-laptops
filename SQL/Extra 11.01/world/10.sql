SELECT name, continent
FROM world AS w1 
WHERE population  >  ALL(SELECT 3* w2.population  FROM world AS w2
WHERE w2.continent = w1.continent
AND w2.name != w1.name);
