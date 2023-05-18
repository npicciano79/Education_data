#inner join on majors and employed_data tables 

SELECT m.major_code,m.major,e.employed 
FROM majors AS m 
INNER JOIN employed_data AS e 
ON m.major_code=e.major_code
GROUP BY m.major_code
ORDER BY m.major_code;