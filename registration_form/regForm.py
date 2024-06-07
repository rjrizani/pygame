import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    country = country_var.get()
    password = password_entry.get()
    comfirm_password = comfirm_password_entry.get()

    if name == "" or email == "" or gender == "" or country == "" or password == "" or comfirm_password == "":
        messagebox.showerror("Error", "Please fill in all fields")
    elif password != comfirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        messagebox.showinfo("Success", "Registration successful")

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg='#E6E6FA')

style = ttk.Style()
style.theme_use('clam')

style.configure("Tlabel", font=("Helvetica", 12), background="#E6E6FA")   #atur warna bg dan font label

style.configure("TEntry", font=("Helvetica", 12), background="white", foreground="black")   #atur warna bg dan font entry

style.configure("TButton", font=("Helvetica", 12), background="white", foreground="black")   #atur warna bg dan font button

style.configure("TCombobox", font=("Helvetica", 12), background="white", foreground="black")   #atur warna bg dan font combobox

name_label = ttk.Label(root, text="Name: ")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = ttk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_label = ttk.Label(root, text="Email: ")
email_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = ttk.Label(root, text="Password: ")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

bio_label = ttk.Label(root, text="Bio: ")
bio_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

bio_entry = ttk.Entry(root, width=30)
bio_entry.grid(row=3, column=1, padx=10, pady=5)

gender_label = ttk.Label(root, text="Gender: ")
gender_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
gender_var = tk.StringVar()
gender_var.set("Male")      #defaul value
male_radio = ttk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
female_radio = ttk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=4, column=1, padx=70, pady=5, sticky=tk.W)

country_var = tk.StringVar()
country_var.set("Indonesia")
country_dropdown = ttk.Combobox(root, textvariable=country_var, values=["USA", "Canada", "Australia", "Rusia"])
country_dropdown.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

comfirm_password = ttk.Label(root, text="Comfirm Password: ")
comfirm_password.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
comfirm_password_entry = ttk.Entry(root, width=30, show="*")
comfirm_password_entry.grid(row=6, column=1, padx=10, pady=5)


submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=7, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

submit_button_style = ttk.Style()
submit_button_style.configure("TButton", font=("Helvetica", 12), background="white", foreground="blue")

submit_button_style.map(
    "TButton",
    foreground=[("pressed", "red"), ("active", "blue")],
    background=[("pressed", "!disabled", "black"), ("active", "white")]
)

submit_button["style"] = "Custom.TButton"



root.mainloop()