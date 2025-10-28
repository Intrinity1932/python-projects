# calci by pawan
import tkinter as tk

window=tk.Tk()



window.geometry("800x500")
window.title("calculator by pawan")



head=tk.Label(window, text="calci by pawan", font=('arial', 20))
head.pack(pady=50)



display=tk.Text(
    window,
    height=2,
    width=50,
    font=('arial', 20)
    )
display.pack()



pad=tk.Frame(window)
pad.columnconfigure(0, weight=1)
pad.pack()



but_clean=tk.Button(pad, text="X", width=20, height=2)
but_del=tk.Button(pad, text="del", width=20, height=2)
but_mul=tk.Button(pad, text="*", width=20, height=2)
but_div=tk.Button(pad, text="/", width=20, height=2)
but1=tk.Button(pad, text="1", width=20, height=2)
but2=tk.Button(pad, text="2", width=20, height=2)
but3=tk.Button(pad, text="3", width=20, height=2)
but_plus=tk.Button(pad, text="+", width=20, height=2)
but4=tk.Button(pad, text="4", width=20, height=2)
but5=tk.Button(pad, text="5", width=20, height=2)
but6=tk.Button(pad, text="6", width=20, height=2)
but_minus=tk.Button(pad, text="-", width=20, height=2)
but7=tk.Button(pad, text="7", width=20, height=2)
but8=tk.Button(pad, text="8", width=20, height=2)
but9=tk.Button(pad, text="9", width=20, height=2)
but_eval=tk.Button(pad, text="=", width=20, height=2)
but_clean.grid(row=0, column=0)
but_del.grid(row=0, column=1)
but_mul.grid(row=0, column=2)
but_div.grid(row=0, column=3)
but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=1, column=2)
but_plus.grid(row=1, column=3)
but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)
but_minus.grid(row=2, column=3)
but7.grid(row=3, column=0)
but8.grid(row=3, column=1)
but9.grid(row=3, column=2)
but_eval.grid(row=3, column=3)



def calci_clean():
    display.delete(1.0, tk.END)

def calci_eval():
    arg=display.get(1.0, tk.END).strip()
    display.delete(1.0, tk.END)
    display.insert(tk.END, eval(arg))

def calci_del():
    arg=display.get(1.0, tk.END).strip()
    display.delete(1.0, tk.END)
    display.insert(tk.END, arg[:-1])



but_clean.config(command=lambda: calci_clean())
but_del.config(command=lambda: calci_del())
but_mul.config(command=lambda: display.insert(tk.END, "*"))
but_div.config(command=lambda: display.insert(tk.END, "/"))
but1.config(command=lambda: display.insert(tk.END, "1"))
but2.config(command=lambda: display.insert(tk.END, "2"))
but3.config(command=lambda: display.insert(tk.END, "3"))
but_plus.config(command=lambda: display.insert(tk.END, "+"))
but4.config(command=lambda: display.insert(tk.END, "4"))
but5.config(command=lambda: display.insert(tk.END, "5"))
but6.config(command=lambda: display.insert(tk.END, "6"))
but_minus.config(command=lambda: display.insert(tk.END, "-"))
but7.config(command=lambda: display.insert(tk.END, "7"))
but8.config(command=lambda: display.insert(tk.END, "8"))
but9.config(command=lambda: display.insert(tk.END, "9"))
but_eval.config(command=lambda: calci_eval())

window.mainloop()
