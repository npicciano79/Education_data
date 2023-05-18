#left join on majors and employed 


SELECT m.major,e.total_students
FROM employed AS e LEFT JOIN majors AS m 
ON m.major_code=e.major_code
ORDER BY total_students DESC;