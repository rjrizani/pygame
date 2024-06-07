import tkinter as tk

window = tk.Tk()

'''
window.title("my first GUI")
greeting = tk.Label(text="Hello, Tkinter",fg="white",bg="black",
                    width=20,height=20)
greeting.pack()

lebel = tk.Label(window, text="Hello sabih")
lebel.config(text= "Hello ahmad sudah termodifikasi")
lebel.config(font=("Arial", 18))
lebel.pack()

def on_button():
    lebel.config(text="Hello ahmad sudah klik button")

button = tk.Button(window, text="click me", command=on_button)
button.pack()
'''
window.title("Counter App")
window.config(bg="lightblue")
def increase():
    global counter
    counter += 1
    lebel.config(text=f"Counter: {counter}")

def decrease():
    global counter
    counter -= 1
    lebel.config(text=f"Counter: {counter}")

counter = 0
lebel = tk.Label(text=f"Counter: {counter}")
lebel.pack(pady=20)

increase_button = tk.Button(text="Increase", command=increase,
                            bg="green", fg="white", font=("Arial", 20),
                            borderwidth=1,relief=tk.RIDGE,
                            activebackground="green",
                            )
increase_button.pack(side="left",pady=20,padx=10)

decrease_button = tk.Button(text="Decrease", command=decrease)
decrease_button.pack(side="left",pady=20, padx=10)





window.mainloop()