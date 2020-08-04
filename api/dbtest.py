import sqlite3
import random


conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.row_factory=sqlite3.Row

cur=conn.cursor()
#conn.execute('CREATE TABLE Projects (Id integer primary key, ProjectName TEXT, CodingHub integer, VisualizationArena integer, AmazingEDA integer)')

cur.execute('''INSERT INTO Projects (ProjectName, CodingHub, VisualizationArena, AmazingEDA)
               VALUES(?, ?, ?, ?)''',('test123',random.randint(0,999999),random.randint(0,999999),random.randint(0,999999)) )
#conn.commit()
print("inserted")

""""cur.execute("INSERT INTO Projects (Projectname, CodingHub, VisualizationArena, AmazingEDA) VALUES ('" + 
		'hello' + "', '" + 
		str(random.randint(0,999999)) + "', '" + 
		str(random.randint(0,999999)) + "', '" + 
		str(random.randint(0,999999)) + "')")
print("inserted")"""
cur.execute('''SELECT * from Projects''')
rows=cur.fetchall()
if(rows):
    for row in rows:
        print(dict(row))
else:
    print("no data!!")
conn.close()
