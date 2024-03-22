from tkinter import *

master = Tk()
master.state('zoomed')
f = Frame(master, width=800, height=400)

Label1 = Label(f, text='Label 1')
Label2 = Label(f, text='Label 2')

f.grid_columnconfigure(0, weight=1)
f.grid_columnconfigure(2, weight=1)
f.grid_columnconfigure(4, weight=1)

Label1.grid(row=0, column=1)
Label2.grid(row=0, column=3)

f.pack()

master.mainloop()
