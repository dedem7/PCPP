#WORKING WITH DB - CREATING USER PROGRAM

import sqlite3
import os

#print(os.getcwd())

def print_menu():
    print("+-----------------------------------+",
      "|              SQL DB               |",
      "+-----------------------------------+",
      "M E N U",
      "=======",
      "1. Show Tasks",
      "2. Add Task",
      "3. Change Priority",
      "4. Delete Task",
      "5. Exit", sep="\n")

def read_user_choice():
    user_choice = input("Enter your choice (1..5): ")
    while user_choice not in ["1","2","3","4","5"]:
        user_choice = input("Enter your choice (1..5): ")
    return user_choice



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
        print("ADDED")
        self.conn.commit()
        return True

    def find_task(self,name):
        try:
            assert name.replace(" ","")!=""
            name = name.strip()
            rows = self.cursor.execute('SELECT * from tasks')
            found = 0
        except AssertionError:
            print("Task name can't be empty")
        except Exception as e:
            print("Here is the error: ", e.message)
            return None
        else:
            for r in rows:
                if r[1] == name:
                    found = 1
                    print(r)
                    return r
            if found == 0:
                return None

    def find_id(self, some_id):
        rows = self.cursor.execute('SELECT * from tasks')
        lst = [r[0] for r in rows]
        if some_id not in lst:
            print("ID not found")
            return False
        else:
            return True
        
    def change_priority(self):
        task_id = 0
        new_priority = 0
        
        while task_id < 1:
            try:
                task_id = int(input("Choose the task id: "))
            except TypeError:
                print("Task ID must be integer")

        if not self.find_id(task_id):
            return None
        
        while new_priority < 1:
            try:
                new_priority = int(input("Choose the new priority: "))
            except TypeError:
                print("Priority must be integer")
                
        try:
            self.cursor.execute('UPDATE tasks SET priority = ? WHERE id = ?',(new_priority,task_id))
        except Exception as e:
            print(e.message)
        else:
            print("UPDATED")
            self.conn.commit()


    def delete_task(self):
        task_id = 0
        
        while task_id < 1:
            try:
                task_id = int(input("Choose the task id: "))
            except TypeError:
                print("Task ID must be integer")

        if not self.find_id(task_id):
            return None
                
        try:
            self.cursor.execute('DELETE FROM tasks WHERE id = ?',(task_id,))
        except Exception as e:
            print(e.message)
        else:
            print("DELETED")
            self.conn.commit()

            
    def show_tasks(self):
        rows = self.cursor.execute('SELECT * from tasks');
        for r in rows:
            print(r)
          
    def close_conn(self):
        self.conn.close()
        print("Connection to DB closed")

#Program launch
to_do = Todo()
while True:
    print_menu()
    choice = read_user_choice()
    if choice == '1':
        to_do.show_tasks()
    elif choice == '2':
        to_do.add_task()
    elif choice == '3':
        to_do.change_priority()
    elif choice == '4':
        to_do.delete_task()
    elif choice == '5':
        to_do.close_conn()
        exit(1)

        
    
