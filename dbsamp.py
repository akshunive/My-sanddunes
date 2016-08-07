import sqlite3
#connecting to the db student (it will be created automatically where the program is stored )
conn=sqlite3.connect('student.db')
#table is created
#conn.execute('create table stud(college varchar(30),name varchar(20),rollno varchar(10) primary key,cgpa float(5.0),dob date,sem1 varchar(13),dept varchar(3))')
#connecting to the db student (it will be created automatically where the program is stored )
conn=sqlite3.connect('student.db')
conn.execute('insert into stud values("CIET","akshaya","001",9.5,1996-05-06,"first","cse")')
conn.execute('insert into stud values("CIET","nive","002",9.9,1996-04-05,"second","cse")')
conn.execute('insert into stud values("CIET","sugan","003",7.8,1996-10-03,"second","cse")')
conn.execute('insert into stud values("KIT","preetha","004",9.9,1997-02-13,"first","ece")')
conn.execute('insert into stud values("GCT","sathya","005",9.9,1996-04-05,"second","cse")')
conn.execute('insert into stud values("CIET","sethu","006",7.8,1996-10-03,"second","cse")')
conn.execute('insert into stud values("KARPAGAM","rupa","007",9.9,1997-02-13,"first","ece")')
conn.commit() #if insert operation is done then it must be commited
conn.close()