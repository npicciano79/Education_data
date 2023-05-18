#uses common table expression to combine majors table 
#and employed_data table

WITH majors_employed_data_CTE(major_code,major_category,major,total_students,employed,FTE,unemployed,unemployed_rate)
AS
(
    SELECT m.major_code,m.major_category,m.major,e.total_students,e.employed,e.FTE,e.unemployed,e.unemployed_rate
    FROM majors AS m, employed_data AS e 
    WHERE m.major_code=e.major_code
)

SELECT *
FROM majors_employed_data_CTE
GROUP BY major_code
ORDER BY major_code;
