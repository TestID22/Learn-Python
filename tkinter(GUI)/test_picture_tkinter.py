from tkinter import *




tk = Tk()
tk.title('Пу')
tk.resizable(0,0)
canvas = Canvas(tk, width=1000, height=900, bd=0)
canvas.pack()
image = PhotoImage(file=r'‪D:\Арт\player1.gif')

class Ball():
    def __init__(self, canvas):
        self.canvas = canvase
        self.id = canvas.create_image(0, 0, anchor = NW, image = image)

    def draw(self):
        pass





ball = Ball(canvas)
while 1:
    tk.update()
    ball.draw()