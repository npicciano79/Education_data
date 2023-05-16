import mysql.connector
import config 


db=mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.password,
)


mycursor=db.cursor()

mycursor.execute("SHOW DATABASES")
databases=mycursor.fetchall()
database_names=[database[0] for database in databases]

print(database_names)

if config.database in database_names:
    print('{} exists.'.format(config.database))
else:
    print('Creating database {}'.format(config.database))
    mycursor.execute("CREATE DATABASE college_majors_db")
