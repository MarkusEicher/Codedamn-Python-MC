import tkinter
from tkinter import ttk

root = tkinter.Tk()

root.title("Codedamn Practice")

style = ttk.Style()
style.configure("Label", foreground="white", background="black")
tkinter.Label(root, text="Hello World!").grid(row=0, column=0, columnspan=3, padx=(10, 20), pady=20)

name = ttk.Entry(root)
name.grid(row=1, column=0, pady=10, padx=10)

def click_me():
    print( name.get() )

btn = ttk.Button(root, text="Submit", command=click_me)
btn.grid(row=1, column=2, pady=10, padx=10)

value = tkinter.StringVar()

def option_changed(option):
    print(option)

options = ["Alice", "Bob", "Charlie"]
menu = ttk.OptionMenu(root, value, *options, command=option_changed)
menu.grid(  row=2, columnspan=3)

value.set(options[0])

root.mainloop()


