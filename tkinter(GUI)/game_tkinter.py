from tkinter import *
import time
import random

class Ball():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 245, 100)
        
        self.y = -1
        start = [-3,2,1,-2,-1,3]
        random.shuffle(start)
        self.x = start[0]
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= 400:
            self.y = -1
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= 500:
            self.x = -1

tk = Tk()
tk.title('GameOfThrones')#Заголовок окна
tk.resizable(0,0) #Неизменяемый размер окна
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness = 0)
canvas.pack()

ball = Ball(canvas, 'green')
while True:
    tk.update()
    ball.draw()
    time.sleep(0.01)
    