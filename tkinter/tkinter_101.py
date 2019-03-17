from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='вирус запушен', message='спасибо')

window = Tk()
button = Button(window, text='Кнопка', command = reply)
button.pack()
window.mainloop()
