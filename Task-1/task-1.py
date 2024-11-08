import tkinter as tk
from tkinter import messagebox

# Task file to store tasks
TASK_FILE = 'tasks.txt'

# Load tasks from the file
def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Add a new task
def add_task():
    task = task_input.get().strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        task_input.delete(0, tk.END)
        refresh_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Remove a task
def remove_task(index):
    del tasks[index]
    save_tasks(tasks)
    refresh_task_list()

# Update a task
def update_task():
    updated_task = update_input.get().strip()
    if updated_task:
        tasks[update_index] = updated_task
        save_tasks(tasks)
        refresh_task_list()
        update_window.destroy()
    else:
        messagebox.showwarning("Input Error", "Please enter the updated task.")

# Show update window
def show_update_task(index):
    global update_index
    update_index = index
    update_input.delete(0, tk.END)
    update_input.insert(0, tasks[index])
    update_window.deiconify()

# Refresh the task list in the UI
def refresh_task_list():
    for widget in task_list_frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        task_item = tk.Frame(task_list_frame)
        task_item.pack(fill='x', pady=5)

        task_label = tk.Label(task_item, text=task, width=25, anchor='w')
        task_label.pack(side='left', padx=5)

        update_button = tk.Button(task_item, text="Update", command=lambda index=index: show_update_task(index))
        update_button.pack(side='left', padx=5)

        delete_button = tk.Button(task_item, text="Delete", command=lambda index=index: remove_task(index))
        delete_button.pack(side='left', padx=5)

# Set up the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")

# Create UI elements
task_input = tk.Entry(root, width=30)
task_input.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_list_frame = tk.Frame(root)
task_list_frame.pack(pady=10)

# Update task window (hidden initially)
update_window = tk.Toplevel(root)
update_window.title("Update Task")
update_window.geometry("300x100")
update_window.withdraw()  # Hidden initially

update_input = tk.Entry(update_window, width=30)
update_input.pack(pady=10)

update_button = tk.Button(update_window, text="Update Task", command=update_task)
update_button.pack()

# Load tasks and display them
tasks = load_tasks()
refresh_task_list()

# Run the application
root.mainloop()
