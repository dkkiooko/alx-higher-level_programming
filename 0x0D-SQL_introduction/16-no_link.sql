-- lists all records of the table in MySQL server
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;

