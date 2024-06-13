import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pytz

#set timezone zone to malaysia
tz = pytz.timezone("Asia/Kuala_Lumpur")

def update_time():
    current_time = datetime.now(tz).strftime(time_format.get())
    label.config(text=current_time)
    label.after(1000, update_time)  #1000ms = 1sec
    check_alarm(current_time)

def set_alarm():
    alarm_time_str = alarm_time.get()
    alarm_datetime = datetime.strptime(alarm_time_str, "%H:%M:%S")
    alarm_hour = alarm_datetime.hour
    alarm_minute = alarm_datetime.minute
    alarm_second = alarm_datetime.second
    alarm_active.set(True)
    alarm_label.config(text="Alarm set for " + alarm_time_str)

def check_alarm(current_time):
    if alarm_active.get() and alarm_time.get() == current_time:
        messagebox.showinfo("Alarm", "Time to Wake up!")
        alarm_active.set(False)
        alarm_label.config(text="")



root = tk.Tk()
root.title("Clock")
root.geometry("400x350")
root.configure(bg="lightblue")

frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor="center")

#create  a lebel to display the time
label = tk.Label(frame, font=("Arial", 50), bg="lightblue", fg="black")
label.pack()

#set the time format
time_format = tk.StringVar()
time_format.set("%H:%M:%S")

alarm_time = tk.StringVar()
alarm_entry = tk.Entry(root, textvariable=alarm_time, width=10)
alarm_entry.pack(padx=10, pady=10)

#create button to set alarm
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(padx=10, pady=10)

alarm_active = tk.BooleanVar()
alarm_active.set(False)
alarm_label = tk.Label(root, text="")
alarm_label.pack(padx=10, pady=10)


update_time()

root.mainloop()