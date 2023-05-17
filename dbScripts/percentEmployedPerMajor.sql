/*
FIND the percent of students from each major that 
are full-time-employed FTE
*/


SELECT m.major AS Major,ROUND((e.FTE/e.total_students)*100,2) AS Percent_employed
FROM majors AS m,
employed_data AS e 
WHERE e.major_code=m.major_code
ORDER BY Percent_employed DESC;