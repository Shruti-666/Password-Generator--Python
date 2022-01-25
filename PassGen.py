from logging import root
import tkinter as tk
from operator import le
import string
import random

from numpy import append

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text="PASSWORD GENERATOR")
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='What length of Password do you want?')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)


def PasswordGenerator():
    char=list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(char)
    x1 = int(entry1.get())

    Pass=[]
    for i in range(x1):
        Pass.append(random.choice(char))

    label3 = tk.Label(root, text= 'Your Password is ',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text= "".join(Pass),font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)

button1 = tk.Button(text='Get Password', command=PasswordGenerator, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()