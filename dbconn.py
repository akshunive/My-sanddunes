#database connectivity in python using sqlite3
import sqlite3
conn=sqlite3.connect('student.db')#selecting or creating a database
cursor.execute('''CREATE TABLE stud(college varchar(50),name varchar(20),roll_no varchar(10),dob date,dept varchar(10))''')#creating a table
conn.execute("INSERT INTO stud VALUES('ciet','nive',001,'1995-23-11','cse')")#inserting first set of values
conn.execute("INSERT INTO stud VALUES('ciet','rupa',002,'1995-12-03','cse')")#inserting second set of values
conn.execute("INSERT  INTO stud VALUES('ciet','sugan',003,'1995-08-16','cse')")#inserting third set of values
conn.commit()#writes the inserted values into the database
cursor=conn.cursor()
cursor.execute("SELECT * FROM stud")#displaying all the attributes from table
print cursor.fetchone()#fetches one record alone
cursor.execute("SELECT * FROM stud WHERE name='rupa'")
print cursor.fetchone()#fetches the next record
cursor.execute("SELECT dob FROM stud")
print cursor.fetchone()
conn.close()