SELECT ROUND(AVG(IF(LENGTH IS NULL, 10, LENGTH)), 2) AS "AVERAGE_LENGTH"
FROM FISH_INFO;