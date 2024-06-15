import tkinter as tk
from tkinter import messagebox

def update_listbox():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, contact["Name"])

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if name and phone and  address:
        contact = {"Name": name, "Phone": phone, "Address": address}
        contacts.append(contact)

        update_listbox()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully")
    else:
        messagebox.showerror("Error", "Please fill in all fields")


def view_details():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        messagebox.showinfo("Contact Details", f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nAddress: {contact['Address']}")
def update_contact():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_name = name_entry.get()
        new_phone = phone_entry.get()
        new_address = address_entry.get()
        if new_name and new_phone and new_address:
            contacts[selected_index]['Name'] = new_name
            contacts[selected_index]['Phone'] = new_phone
            contacts[selected_index]['Address'] = new_address
            update_listbox()
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            address_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Name, phone, and address fields are required.")

def delete_contact():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        contacts.remove(contact)

        update_listbox()
        messagebox.showinfo("Success", "Contact deleted successfully")

root = tk.Tk()
root.title("Address Book")

contacts = []
name_label = tk.Label(root, text="Name: ")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Phone: ")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

address_label = tk.Label(root, text="Address: ")
address_label.grid(row=2, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Add", command=add_contact)
add_button.grid(row=3, column=0)

contacts_listbox = tk.Listbox(root)
contacts_listbox.grid(row=4, column=0, columnspan=2)

view_button = tk.Button(root, text="View Details", command=view_details)
view_button.grid(row=5, column=0)

update_button = tk.Button(root, text="Update", command=update_contact)
update_button.grid(row=5, column=1)

delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=5, column=1)




root.mainloop()