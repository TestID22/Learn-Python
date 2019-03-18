from tkinter import *
from tkinter.messagebox import showinfo
import os

def reply():
    showinfo(title='вирус запушен', message='спасибо')
    os.system('ping google.com')

window = Tk()
button = Button(window, text='Google - держись', command = reply)
button.pack()
window.mainloop()
