-- import database table dump
-- write a scipt that diplays max temp of each state ASC
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`
;

