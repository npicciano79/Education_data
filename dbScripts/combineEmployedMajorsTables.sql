#USES common table expressons to combine
#employed and majors tables


WITH major_employed_CTE (major_code,major_category,major,total_students,employed)
AS 
    (
    SELECT e.major_code,m.major_category,m.major,e.total_students,e.employed
    FROM employed AS e, majors AS m 
    WHERE m.major_code=e.major_code
    )
SELECT major_code,major_category
FROM major_employed_CTE
GROUP BY major_code
ORDER BY major_code;
