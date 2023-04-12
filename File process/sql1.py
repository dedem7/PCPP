#CREATE A TASK, ASKING A USER TO PROVIDE INPUT AND ADD TO DB (SQL)

import sqlite3
import os

print(os.getcwd())
class Todo:
    def __init__(self):
        self.conn = sqlite3.connect("Database_todo.db")
        self.cursor = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    priority INTEGER NOT NULL);''')

    def add_task(self):
        name = ""
        while name.replace(" ","") == "":
            name = input("Enter task name: ")
        if self.find_task(name):
            print("This task is already exists")
            return None   
        priority = 0
        while priority < 1:   
            try:
                priority = int(input("Enter priority: "))
            except:
                print("Priority must be integer")
        
        self.cursor.execute('INSERT INTO tasks (task, priority) VALUES (?,?)',(name,priority))
        self.conn.commit()
        return True

    def find_task(self,name):
        try:
            assert name.replace(" ","")!=""
            name = name.strip()
            rows = self.cursor.execute('SELECT * from tasks');
            found = 0
        except AssertionError:
            print("Task name can't be empty")
        except Exception as e:
            print("Here is the error: ", e.message)
        else:
            for r in rows:
                if r[1] == name:
                    found = 1
                    print(r)
                    return r
            if found == 0:
                print("Not found")
                return None

    def show_tasks(self):
        rows = self.cursor.execute('SELECT * from tasks');
        for r in rows:
            print(r)
          
    def close_conn(self):
        self.conn.close()
        print("Connection to DB closed")
        
        
to_do = Todo()
to_do.add_task()
to_do.close_conn()


###--- fetchall to create a list of all records
##
##import sqlite3
##
##conn = sqlite3.connect('todo.db')
##c = conn.cursor()
##c.execute('SELECT * FROM tasks')
##rows = c.fetchall()
##for row in rows:
##    print(row)
##conn.close()
##
##
###---fetchone to return next row
##import sqlite3
##
##conn = sqlite3.connect('todo.db')
##c = conn.cursor()
##c.execute('SELECT * FROM tasks')
##row = c.fetchone()
##print(row)
##row = c.fetchone()
##print(row)
##conn.close()
