SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia');

-- 2

-- 3 
SELECT name, continent 
FROM  world
WHERE continent IN (SELECT continent 
FROM world WHERE name  IN ("Argentina", "Australia")) 
ORDER BY name;



