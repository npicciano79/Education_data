


SELECT m.major AS Major,e.employed AS Employed
FROM majors AS m 
    LEFT JOIN employed AS e 
    ON e.major_code=m.major_code
WHERE e.employed>=10000
ORDER BY Employed DESC;



