import tkinter as tk
import time

running = False
paused = False
start_time = 0
time_diff = 0

window = tk.Tk()
window.geometry("800x500")
window.title('stopwatch')

time_label = tk.Label(window, text="00:00:00.00", font=('arial', 40))
time_label.pack(pady=100)

buttons = tk.Frame(window)
buttons.pack()

but1 = tk.Button(buttons, text='start', height=2, width=15)
but2 = tk.Button(buttons, text='stop', height=2, width=15)
but3 = tk.Button(buttons, text='reset', height=2, width=15)

but1.grid(row=0, column=0)
but2.grid(row=0, column=1)
but3.grid(row=0, column=2)

def time_fun():
    if running:
        elapsed = (time.time() - start_time) + time_diff
        sec = int(elapsed % 60)
        mins = int((elapsed // 60) % 60)
        hrs = int(elapsed // 3600)
        m_sec = int((elapsed * 100) % 100)

        time_label.config(text=f"{hrs:02d}:{mins:02d}:{sec:02d}.{m_sec:02d}")
        window.after(10, time_fun)

def start():
    global running, start_time, paused
    if not running:
        start_time = time.time()
        running = True
        paused = False
        time_fun()

def stop():
    global running, time_diff
    if running:
        running = False
        time_diff += (time.time() - start_time)

def reset():
    global running, time_diff
    if not running:
        time_diff = 0
        time_label.config(text="00:00:00.00")

but1.config(command=start)
but2.config(command=stop)
but3.config(command=reset)

window.mainloop()
