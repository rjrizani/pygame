import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pytz

# import required module
from playsound import playsound


playsound("stab-f-01-brvhrtz-224599.mp3")
print('playing sound using  playsound')

jakarta = pytz.timezone('Asia/Jakarta')

def update_time():
    current_time= datetime.now(jakarta).strftime(time_format.get())
    label.config(text=current_time)
    label.after(1000, update_time)
    check_alarm(current_time)


def set_alarm():
    alarm_time_str = alarm_time.get()
    alarm_datetime = datetime.strptime(alarm_time_str, '%H:%M:%S')
    alarm_hour = alarm_datetime.hour
    alarm_minute = alarm_datetime.minute
    alarm_second = alarm_datetime.second
    print(alarm_time_str, alarm_hour, alarm_minute, alarm_second)
    alarm_label.config(text=f"Alarm set for {alarm_time_str}")

def check_alarm(current_time):
    if alarm_time.get() == current_time:
        messagebox.showinfo("Alarm", "Wake up!")


root = tk.Tk()
root.title("Clock")
root.geometry("400x200")
root.configure(bg="#FFC0CB")

label = tk.Label(root, text="Clock", bg="lightblue", fg="black")
label.config(font=("Arial", 24))
label.pack(pady=20)

time_format = tk.StringVar()
time_format.set('%H:%M:%S')

alarm_time =tk.StringVar()
alarm_entry = tk.Entry(root, textvariable=alarm_time, width=10)
alarm_entry.pack(pady=10)

#create button to set alarm
btn_set = tk.Button(root, text="Set Alarm", bg="green", fg="white", command=set_alarm)
btn_set.pack(pady=10)

alarm_active = tk.BooleanVar()
alarm_active.set(False)

alarm_label = tk.Label(root, text="", bg="lightblue", fg="black")
alarm_label.pack(pady=10)


update_time()


root.mainloop()
