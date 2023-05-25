#returns employment percentage for majors with less that 10000 total students

SELECT m.major_code,m.major,e.total_students,ROUND((e.employed/e.total_students)*100,2) AS percent_employed
FROM majors AS m, employed AS e 
WHERE m.major_code=e.major_code
AND e.total_students<10000
GROUP BY major_code
ORDER BY percent_employed DESC;