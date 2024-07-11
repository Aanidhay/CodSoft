import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.todo_list = []

        # frames
        self.input_frame = tk.Frame(root, bg="#f0f0f0")
        self.input_frame.pack(fill="x", padx=10, pady=10)

        self.list_frame = tk.Frame(root, bg="#f0f0f0")
        self.list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # input fields and buttons
        self.task_label = tk.Label(self.input_frame, text="Task:", font=("Times New Roman", 12))
        self.task_label.pack(side="left", padx=5)

        self.task_entry = tk.Entry(self.input_frame, width=30, font=("Times New Roman", 12))
        self.task_entry.pack(side="left", padx=5)

        self.add_button = tk.Button(self.input_frame, text="Add Task", command=self.add_task, font=("Times New Roman", 12))
        self.add_button.pack(side="left", padx=5)

        self.delete_button = tk.Button(self.input_frame, text="Delete Task", command=self.delete_task, font=("Times New Roman", 12))
        self.delete_button.pack(side="left", padx=5)

        self.search_label = tk.Label(self.input_frame, text="Search:", font=("Times New Roman", 12))
        self.search_label.pack(side="left", padx=5)

        self.search_entry = tk.Entry(self.input_frame, width=20, font=("Times New Roman", 12))
        self.search_entry.pack(side="left", padx=5)

        self.search_button = tk.Button(self.input_frame, text="Search", command=self.search_task, font=("Times New Roman", 12))
        self.search_button.pack(side="left", padx=5)

        # list box and scrollbar
        self.task_listbox = tk.Listbox(self.list_frame, width=30, height=10, font=("Times New Roman", 12))
        self.task_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side="right", fill="y", padx=5, pady=5)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.task_listbox.bind('<Double-1>', self.edit_task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task")

    def delete_task(self):
        try:
            task_number = self.task_listbox.curselection()[0]
            del self.todo_list[task_number]
            self.task_listbox.delete(task_number)
        except IndexError:
            messagebox.showerror("Error", "Please select a task to delete")

    def search_task(self):
        self.task_listbox.delete(0, tk.END)
        search_term = self.search_entry.get()
        for task in self.todo_list:
            if search_term.lower() in task.lower():
                self.task_listbox.insert(tk.END, task)

    def edit_task(self, event):
        task_number = self.task_listbox.curselection()[0]
        task = self.task_listbox.get(task_number)
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(0, task)
        self.task_entry.focus()

        def save_edits():
            new_task = self.task_entry.get()
            if new_task:
                self.todo_list[task_number] = new_task
                self.task_listbox.delete(task_number)
                self.task_listbox.insert(task_number, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please enter a new task")

        self.add_button.config(text="Save", command=save_edits)

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()