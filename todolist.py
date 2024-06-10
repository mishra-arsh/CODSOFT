import tkinter as tk
from tkinter import messagebox

# Add Task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Delete Task
def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

# Udate task
def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task != "":
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, updated_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

root = tk.Tk()
root.title("To-Do List")

# This will create a label and an entry field for new tasks
label_task = tk.Label(root, text="Task:")
label_task.pack()

entry_task = tk.Entry(root, width=50)
entry_task.pack()

# This will create a listbox to display tasks
listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

# This will create buttons for adding, updating, and deleting tasks
button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack()

button_update_task = tk.Button(root, text="Update Task", command=update_task)
button_update_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack()

root.mainloop()