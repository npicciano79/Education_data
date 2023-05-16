import mysql.connector
import csv
import config 

cleanCSV="collegemajordata.csv"


db=mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.password,
    database=config.database,
   
)
mycursor=db.cursor()

insert_statement=(
    "INSERT INTO majors(major_code,major,major_category)\
    VALUES (%s,%s,%s)"
)
"""
#inserts data into majors
with open(cleanCSV,mode='r')as csv_data:
    reader=csv.reader(csv_data,delimiter=',')
    csv_data_list=list(reader)
    for row in csv_data_list[1:]:
        col1=row[0]
        col2=row[1]
        col3=row[2]
        mycursor.execute("INSERT INTO majors(major_code,major,major_category)\
                            VALUES (%s,%s,%s)",(col1,col2,col3))

print('majors_data inserted')
"""
#inserts data into  employed_data
with open(cleanCSV,mode='r')as csv_data:
    reader=csv.reader(csv_data,delimiter=',')
    csv_data_list=list(reader)
    for row in csv_data_list[1:]:
        col1=row[0]
        col2=row[3]
        col3=row[4]
        col4=row[5]
        col5=row[6]
        col6=row[7]
        mycursor.execute("INSERT INTO employed_data(major_code,total_students,employed,FTE,unemployed,unemployed_rate)\
                            VALUES (%s,%s,%s,%s,%s,%s)",(col1,col2,col3,col4,col5,col6))
        
print('employee_data inserted')
#inserts data into employed
with open(cleanCSV,mode='r')as csv_data:
    reader=csv.reader(csv_data,delimiter=',')
    csv_data_list=list(reader)
    for row in csv_data_list[1:]:
        col1=row[0]
        col2=row[3]
        col3=row[4]
        mycursor.execute("INSERT INTO employed(major_code,total_students,employed)\
                            VALUES (%s,%s,%s)",(col1,col2,col3))
print('employee inserted')



db.commit()
mycursor.close()
db.close()
print('finished')