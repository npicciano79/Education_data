import mysql.connector
import config 


db=mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.password,
    database=config.database,
)


mycursor=db.cursor()



mycursor.execute("CREATE TABLE IF NOT EXISTS majors\
                    (major_code SMALLINT NOT NULL,\
                     major varchar(200) NOT NULL,\
                     major_category varchar(200) NOT NULL,\
                     PRIMARY KEY(major_code)\
                    )ENGINE=InnoDB")


mycursor.execute("CREATE TABLE IF NOT EXISTS employed\
                    (major_code SMALLINT NOT NULL,\
                    total_students INT NOT NULL,\
                     employed INT NOT NULL,\
                     PRIMARY KEY(major_code)\
                    )ENGINE=InnoDB")

mycursor.execute("CREATE TABLE IF NOT EXISTS employed_data\
                 (major_code SMALLINT NOT NULL,\
                 total_students INT NOT NULL,\
                 employed INT NOT NULL,\
                 FTE INT,\
                 unemployed INT,\
                 unemployed_rate INT,\
                 PRIMARY KEY(major_code)\
                 )ENGINE=InnoDB")



