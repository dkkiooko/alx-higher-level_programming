-- list all records with a score >= 10 in MySQL database
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

