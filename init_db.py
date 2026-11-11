import sqlite3
conn=sqlite3.connect('todo.db')
cursor=conn.cursor()


cursor.execute('''
   CREATE TABLE IF NOT EXISTS todos(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   task TEXT NOT NULL)
''')

seed =['learn Flask','learn sql','build a project']
for task in seed:
    cursor.execute("INSERT INTO todos (task) VALUES(?)",(task,))

 
conn.commit()
conn.close()
print("Database Ready")