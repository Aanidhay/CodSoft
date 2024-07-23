import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

        # Create labels and entries
        tk.Label(self.frame1, text="Name:").pack(side=tk.LEFT)
        self.name_entry = tk.Entry(self.frame1, width=20)
        self.name_entry.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Phone:").pack(side=tk.LEFT)
        self.phone_entry = tk.Entry(self.frame1, width=20)
        self.phone_entry.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Email:").pack(side=tk.LEFT)
        self.email_entry = tk.Entry(self.frame1, width=20)
        self.email_entry.pack(side=tk.LEFT)
        tk.Label(self.frame1, text="Address:").pack(side=tk.LEFT)
        self.address_entry = tk.Entry(self.frame1, width=20)
        self.address_entry.pack(side=tk.LEFT)

        # Create buttons
        tk.Button(self.frame2, text="Add Contact", command=self.add_contact).pack(side=tk.LEFT)
        tk.Button(self.frame2, text="View Contacts", command=self.view_contacts).pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Search Contact", command=self.search_contact).pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Update Contact", command=self.update_contact).pack(side=tk.LEFT)
        tk.Button(self.frame2, text="Delete Contact", command=self.delete_contact).pack(side=tk.LEFT)

        # Create listbox
        self.listbox = tk.Listbox(self.frame3, width=40)
        self.listbox.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            if name in self.contacts:
                messagebox.showerror("Error", "Contact already exists")
            else:
                self.contacts[name] = {"phone": phone, "email": email, "address": address}
                self.listbox.insert(tk.END, f"{name} - {phone}")
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.address_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter name and phone number")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.listbox.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        search_term = self.name_entry.get()
        self.listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details["phone"]:
                self.listbox.insert(tk.END, f"{name} - {details['phone']}")

    def update_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            name = self.listbox.get(selected_index)
            name = name.split(" - ")[0]
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, f"{name} - {self.contacts[name]['phone']}")

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            name = self.listbox.get(selected_index)
            name = name.split(" - ")[0]
            if messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}?"):
                del self.contacts[name]
                self.listbox.delete(selected_index)

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()