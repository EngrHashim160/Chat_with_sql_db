import sqlite3


## connect to sqlite
connection = sqlite3.connect("student.db")

## create a cursor object to insert record, create table

cursor = connection.cursor()

## creating the table
table_info = """
create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""

## Execute query
cursor.execute(table_info)


## Let's insert some records
cursor.execute('''Insert Into STUDENT values('Hashim', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Izaz', 'Data Science', 'B', 80)''')
cursor.execute('''Insert Into STUDENT values('Abubakar', 'Devops', 'A-', 85)''')
cursor.execute('''Insert Into STUDENT values('Sohail', 'Network Communication', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Adil', 'Web Development', 'A', 90)''')

## Display all the records
print("The Inserted Records are: ")
data = cursor.execute('''Select * from STUDENT''')
for record in data:
    print(record)
    
## commit changes in the databases
connection.commit()


## close the connection
connection.close()