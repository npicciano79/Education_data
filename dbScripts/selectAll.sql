#select majors with employment greater than 20000


SELECT *
FROM employed_data
WHERE employed>20000
ORDER BY employed DESC;