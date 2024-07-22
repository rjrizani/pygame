import tkinter as tk


#create window and title
app = tk.Tk()
app.title("Weight Conversion")
app.geometry("400x250")

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

    selected_unit = unit_choices.get()
    print(weight, selected_unit)
    result_text.set("")

    if selected_unit == "Kilograms to pounds":
        result = float(weight) * 2.20462
        print("terbacan", result)
        result_text.set(f"{result} pounds")



#create button to convert
btn_convert = tk.Button(app, text="Convert", bg="green", fg="white", command=convert_weight)
btn_convert.config(font=("Arial", 18))
btn_convert.pack(pady = 5)


#result label
result_text = tk.StringVar()

result_label = tk.Label(app, text=result_text, bg="lightblue", fg="black")
result_label.config(font=("Arial", 18))
result_label.pack(pady = 5)



app.mainloop()
