try:
    import tkinter as tk
    from tkinter import messagebox
except ModuleNotFoundError:
    print("Error: Tkinter module is not available in this environment.")
    exit()

# Creating main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Ensure task_listbox is initialized before any function uses it
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    if task_listbox.size() > 0:
        selected_task = task_listbox.curselection()
        if selected_task:
            task_listbox.delete(selected_task[0])
        else:
            messagebox.showwarning("Warning", "No task selected!")
    else:
        messagebox.showwarning("Warning", "Task list is empty!")

def update_task():
    if task_listbox.size() > 0:
        selected_task = task_listbox.curselection()
        updated_task = task_entry.get().strip()
        if selected_task:
            if updated_task:
                task_listbox.delete(selected_task[0])
                task_listbox.insert(selected_task[0], updated_task)
                task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Updated task cannot be empty!")
        else:
            messagebox.showwarning("Warning", "No task selected!")
    else:
        messagebox.showwarning("Warning", "Task list is empty!")

def clear_tasks():
    if task_listbox.size() > 0:
        task_listbox.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task list is already empty!")

# Input field and buttons
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.grid(row=0, column=1, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks)
clear_button.grid(row=0, column=3, padx=5)

# Running the application
root.mainloop()
