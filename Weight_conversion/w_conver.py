import tkinter as tk


#create window and title
app = tk.Tk()
app.title("Weight Conversion")
app.geometry("500x250")

#set background color
app.configure(bg="lightblue")

lebel = tk.Label(app, text="Enter Weight", bg="lightblue", fg="black")
lebel.config(font=("Arial", 18))
lebel.pack(pady = 5)

#create entry weight
entry_weight = tk.Entry(app, bg="white", fg="black")
entry_weight.config(font=("Arial", 18))
entry_weight.pack(pady = 5)

unit_choices = tk.StringVar(app)
unit_choices.set("Kilograms to pounds")
unit_options = ["Kilograms to pounds", "Pounds to kilograms", "Kilograms to ounces", "Ounces to kilograms"]

drop = tk.OptionMenu(app, unit_choices, *unit_options)
drop.pack(pady = 5)

def convert_weight():
    weight = entry_weight.get()
    print(type(weight))
    selected_unit = unit_choices.get()
    print(weight, selected_unit)
    result_text.set("")

    weight = float(weight)

    if selected_unit == "Kilograms to pounds":
        result = weight * 2.205
        result_text.set(f"{weight:.2f} kilograms is equal to {result:.2f} pounds")
    elif selected_unit == "Pounds to kilograms":
        result = weight / 2.205
        result_text.set(f"{weight:.2f} pounds is equal to {result:.2f} kilograms")
    elif selected_unit == "Kilograms to ounces":
        result = weight * 35.274
        result_text.set(f"{weight:.2f} kilograms is equal to {result:.2f} ounces")
    elif selected_unit == "Ounces to kilograms":
        result = weight / 35.274
        result_text.set(f"{weight:.2f} ounces is equal to {result:.2f} kilograms")



#create button to convert
btn_convert = tk.Button(app, text="Convert", bg="green", fg="white", command=convert_weight)
btn_convert.config(font=("Arial", 18))
btn_convert.pack(pady = 5)


#result label
result_text = tk.StringVar()

result_label = tk.Label(app, textvariable=result_text, bg="lightblue", fg="black")
result_label.config(font=("Arial", 18))
result_label.pack(pady = 5)



app.mainloop()
