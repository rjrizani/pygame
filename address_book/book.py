import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Address Book")
#root.geometry("400x200")
root.configure(bg="lightblue")

contacts = []

def update_contacts():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, contact)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if name and phone and address:
        contact = {"name": name, "phone": phone, "address": address}
        contacts.append(contact)
        update_contacts()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully")
    else:
        messagebox.showerror("Error", "Please fill in all fields")




name_label = tk.Label(root, text="Name: ", bg="lightblue", fg="black")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(root, text="Phone: ", bg="lightblue", fg="black")
phone_label.grid(row=1, column=0, padx=10, pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

address_label = tk.Label(root, text="Address: ", bg="lightblue", fg="black")
address_label.grid(row=2, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add", bg="green", fg="white", command=add_contact)
add_button.grid(row=3, column=0, padx=10, pady=10)

contacts_listbox = tk.Listbox(root)
contacts_listbox.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

update_contacts()

def delete_contact():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del contacts[selected_index]
        update_contacts()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact deleted successfully")

def view_details():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        messagebox.showinfo("Details", f"Name: {contact['name']}\nPhone: {contact['phone']}\nAddress: {contact['address']}")
    else:
        messagebox.showerror("Error", "Please select a contact")

view_button = tk.Button(root, text="View", bg="blue", fg="white", command=view_details)
view_button.grid(row=5, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete", bg="red", fg="white", command=delete_contact)
delete_button.grid(row=5, column=1, padx=10, pady=10)

update_button = tk.Button(root, text="Update", bg="orange", fg="white")
update_button.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()