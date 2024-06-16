''' 
 A To-Do List application is a useful project that helps users manage
 and organize their tasks efficiently. This project aims to create a
 command-line or GUI-based application using Python, allowing
 users to create, update, and track their to-do lists

'''
## importing the required libraries
import sqlite3
import tkinter as tk
from tkinter import messagebox


## seting up the database to store and manage task
def create_db():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    ''')
    conn.commit()
    return conn

## defining functions to create and manipulate task in database
def add_task(conn, description):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description, completed) VALUES (?, ?)', (description, False))
    conn.commit()

def remove_task(conn, id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()

def update_task(conn, id, new_description):
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET description = ? WHERE id = ?', (new_description, id))
    conn.commit()

def view_tasks(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    return cursor.fetchall()

def mark_complete(conn, id, completed):
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (completed, id))
    conn.commit()


## Setup GUI (Tkinter) , linking buttons to the core functions for task management.
class ToDoApp:
    
    def __init__(self, window, conn):
        self.window = window
        self.conn = conn
        self.window.title("To-Do List")
# # A canvas is created and used to draw the gradient background.
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()
        self.refresh_tasks()

# #  Widgets such as Label, Entry, Button, and Listbox are created
    def create_widgets(self):
        self.label = tk.Label(self.window, text="To-Do List", font=('Helvetica', 16, 'bold'), bg="#5DF233" )
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.window, width=50)
        self.entry.pack(pady=5)
        
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)    

        self.task_listbox = tk.Listbox(self.window, width=50, height=10)
        self.task_listbox.pack(pady=5)
        
        self.complete_button = tk.Button(self.window, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)
        
        self.remove_button = tk.Button(self.window, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        self.update_button = tk.Button(self.window, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

# # Widgets  are placed on top of the canvas using create_window.

        self.canvas.create_window(200, 30, window=self.label)
        self.canvas.create_window(200, 70, window=self.entry)
        self.canvas.create_window(200, 110, window=self.add_button)
        self.canvas.create_window(200, 200, window=self.task_listbox)
        self.canvas.create_window(200, 330, window=self.complete_button)
        self.canvas.create_window(200, 370, window=self.remove_button)
        self.canvas.create_window(200, 410, window=self.update_button)

        self.apply_gradient()

# # gradient function is created to apply color gradient from green to white to make the interface attractive.   
    def apply_gradient(self):
        width = 400
        height =430
        self.canvas.config(width=width, height=height)
        start_color = (93, 242, 51)  # RGB values for green
        end_color = (255, 255, 255)  # RGB values for white
        
        for i in range(height):
            r = start_color[0] + (end_color[0] - start_color[0]) * i // height
            g = start_color[1] + (end_color[1] - start_color[1]) * i // height
            b = start_color[2] + (end_color[2] - start_color[2]) * i // height
            color = '#%02x%02x%02x' % (r, g, b)
            self.canvas.create_line(0, i, width, i, fill=color)

# # functions in the ToDoApp class are linked to buttons to perform desired actions on the task in the listbox.

    def add_task(self):
        description = self.entry.get()
        if description:
            add_task(self.conn, description)
            self.refresh_tasks()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty task", "Task description cannot be empty.")
    
    def remove_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            id = self.task_listbox.get(selected_task).split(': ')[0]
            remove_task(self.conn, id)
            self.refresh_tasks()
        else:
            messagebox.showwarning("None Selected", "Please select a task to remove.")
    
    def update_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            id = self.task_listbox.get(selected_task).split(': ')[0]
            new_description = self.entry.get()
            if new_description:
                update_task(self.conn, id, new_description)
                self.refresh_tasks()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Empty Task", "New task description cannot be empty.")
        else:
            messagebox.showwarning("None Selected", "Please select a task to update.")
    
    def mark_complete(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            id = self.task_listbox.get(selected_task).split(': ')[0]
            current_status = self.task_listbox.get(selected_task).split(' - ')[1]
            new_status = not (current_status == "Complete")
            mark_complete(self.conn, id, new_status)
            self.refresh_tasks()
        else:
            messagebox.showwarning("None Selected", "Please select a task to mark as complete.")
    
    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = view_tasks(self.conn)
        for task in tasks:
            status = "Complete" if task[2] else "Incomplete"
            self.task_listbox.insert(tk.END, f"{task[0]}: {task[1]} - {status}")


# Initialize the application
conn = create_db()
window = tk.Tk()
app = ToDoApp(window, conn)
window.mainloop()
conn.close()
