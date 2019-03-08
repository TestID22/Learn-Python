import sys
from tkinter import Button, mainloop

x = Button(text='Prss ME', 
           command = (lambda:sys.stdout.write('Spamm')))
x.pack()
mainloop()