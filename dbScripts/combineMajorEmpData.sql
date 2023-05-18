
#common table expresson to combine tables, majors, employed_data
#employed on major_code

WITH full_major_CTE (major_code,major_category,major,total_students,employed,FTE,unemployed,unemployed_rate)
AS 
(
    SELECT DISTINCT m.major_code,m.major_category,m.major,d.total_students,e.employed,d.FTE,d.unemployed,d.unemployed_rate
    FROM majors AS m, employed AS e, employed_data AS d 
    WHERE m.major_code=e.major_code
    AND m.major_code=d.major_code

)
SELECT * 
FROM full_major_CTE
GROUP BY major_code
ORDER BY major_code ASC;
