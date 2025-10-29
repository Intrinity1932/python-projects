import tkinter as tk

hour=00
minute=00
second=0
runner=False

t="00:00:00"

window=tk.Tk()

window.title("stopwatch by pawan")
window.geometry("800x500")

time_label=tk.Label(window, text=t, font=('arial', 40))
time_label.pack(pady=100)

def time_call():
    global hour, minute, second, runner
    if runner:
        second+=1
        if second==60:
            second=0
            minute+=1
        if minute==60:
            minute=0
            hour+=1
        time_label.config(text=f"{hour}:{minute}:{second}")
        window.after(1000, time_call)

def start():
    global runner
    runner=True
    time_call()

def stop():
    global runner
    runner=False

def reset():
    global runner, hour, minute, second
    runner=False
    hour=00
    minute=00
    second=00
    time_label.config(text="00:00:00")
    

grid=tk.Frame(window)
grid.pack()

but1=tk.Button(grid, text='start', height=2, width=20)
but2=tk.Button(grid, text='stop', height=2, width=20)
but3=tk.Button(grid, text='reset', height=2, width=20)
but1.grid(row=0, column=0)
but2.grid(row=0, column=1)
but3.grid(row=0, column=2)

but1.config(command=start)
but2.config(command=stop)
but3.config(command=reset)

window.mainloop()
