import tkinter as tk
from playsound import playsound
import time

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

count = 0


def increase():
    global count
    count += 1
    label.config(text="Counter: " + str(count))




def decrease():
    global count
    count -= 1
    label.config(text="Counter: " + str(count))


label = tk.Label(text="Counter: ", bg="red", fg="white", font=("Arial", 20))
label.pack(pady = 10)

increase_button = tk.Button(text="increase", bg="green", fg="white", font=("Arial", 20), command = increase)
increase_button.pack(side=tk.LEFT, padx = 10, pady = 20)

decrease_button = tk.Button(text="decrease", bg="blue", fg="white", font=("Arial", 20), command= decrease)
decrease_button.pack(side=tk.LEFT, padx = 10, pady = 20)

window.mainloop()
