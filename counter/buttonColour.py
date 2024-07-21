import tkinter as tk

window = tk.Tk()
window.geometry("400x200")

window.title("button event change colour")
colors = ["red", "green", "blue", "yellow", "purple"]
count = 0
window.config(bg=colors[count])



def button_click():
    global count
    count += 1
    if count >= len(colors):
        count = 0
    window.config(bg=colors[count])
    print("Tombol ditekan!")

label = tk.Label(window, text="Click button then background colour will change", bg="lightblue", fg="black")
label.pack(pady=20)

button = tk.Button(window, text="Klik Saya", command=button_click)
button.pack(side=tk.TOP, expand=True)



window.mainloop()