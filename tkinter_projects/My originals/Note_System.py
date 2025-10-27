# requirment is tkinter only

import tkinter as tk
from tkinter import simpledialog

window=tk.Tk()

# global note
notes = dict()

# tab info
window.geometry("800x500")
window.title("notes")
window['bg']='black'

# head text
ht=tk.Label(window, text="NOTE - SYSTEM", font=('arial', 20))
ht.pack()

# main display
display=tk.Text(
    window,
    bg='grey',
    height=5,
    width=50,
    highlightbackground='blue',
    highlightthickness='1'    
)
display.pack(pady=50)

# for add and search
aas = tk.Frame(window)
aas.columnconfigure(0, weight=1)
aas.columnconfigure(1, weight=1)
aas.pack(pady=20)

# button assigning
but1=tk.Button(aas, text="Add Note")
but2=tk.Button(aas, text="Search Note")
but3=tk.Button(aas, text='show')
but4=tk.Button(aas, text='Clear')
but1.grid(row=0, column=0)
but2.grid(row=0, column=1)
but3.grid(row=1, column=0)
but4.grid(row=1, column=1)

# functionality
def add():
    content=display.get(1.0, tk.END).strip()
    if not content:
        return

    title=simpledialog.askstring('add note', 'add note title')
    if title:
        notes[title]=content

    display.delete(1.0, tk.END)

def search():
    title=simpledialog.askstring('search note', 'enter title here')
    if title in notes:
        display.delete(1.0, tk.END)
        display.insert(tk.END, notes[title])
    else:
        display.delete(1.0, tk.END)
        display.insert(tk.END, 'note with title note found')

def show():
    display.delete(1.0, tk.END)
    for note in notes:
        display.insert(tk.END, f"\ntitle: {note} \nnote: {notes[note]}\n")
def clear():
    display.delete(1.0, tk.END)

but1.config(command=add)
but2.config(command=search)
but3.config(command=show)
but4.config(command=clear)

window.mainloop()
