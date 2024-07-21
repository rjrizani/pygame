import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



root = tk.Tk()
root.title("Registration Form")
root.configure(background="lavender")

# create a style
style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", foreground="black", background="white")
style.configure("TLabel", foreground="black", background="lavender")
style.configure("TButton", foreground="white", background="red", font=("Arial", 14))
style.configure("TCombobox", foreground="black", background="lavender")

def submit():
    print("test berhasil")

name_label = ttk.Label(root, text="Name: ")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

email_label = ttk.Label(root, text="Email: ")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

#create password label
password_label = ttk.Label(root, text="Password: ")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

#create password comfirmation label
confirm_password_label = ttk.Label(root, text="Confirm Password: ")
confirm_password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

#create gender label
gender_label = ttk.Label(root, text="Gender: ")
gender_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

#create country label
country_label = ttk.Label(root, text="Country: ")
country_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

#create bio label
bio_label = ttk.Label(root, text="Bio: ")
bio_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

#buat text input untuk setiap lebelnya seperti diatas
name_entry = ttk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_entry = ttk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_entry = ttk.Entry(root, width=30, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

confirm_password_entry = ttk.Entry(root, width=30, show="*")
confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

# create country combobox
country_combobox = ttk.Combobox(root, width=28)
country_combobox['values'] = ('Indonesia', 'Malaysia', 'Singapore', 'Thailand')
country_combobox.grid(row=5, column=1, padx=10, pady=10)

#create radiobutton for gender
gender_var = tk.StringVar()
gender_var.set("Male")
male_radio = ttk.Radiobutton(root, text="Male", value="Male", variable=gender_var)
male_radio.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

female_radio = ttk.Radiobutton(root, text="Female", value="Female", variable=gender_var)
female_radio.grid(row=4, column=1, padx=70, pady=10, sticky=tk.W)

# create a text box
bio_textbox = tk.Text(root, width=30, height=5)
bio_textbox.grid(row=6, column=1, padx=10, pady=10)

#creat a submit button with style
submit_button = ttk.Button(root, text="Submit", cursor="hand2", style="TButton", command=submit)
submit_button.grid(row=7, column=1, padx=10, pady=10)






root.mainloop()
