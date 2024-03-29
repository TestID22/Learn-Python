from tkinter import *
import sys
import time
import random

class Ball():
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 200, 100) # двигаем объект
        #Управление движением шаром, в главном цикле игры будет отображаеться 
        #перемещение шара на self.x и sel.y координат соответвенно
        self.y = -1
        start = [-3,2,1,-2,-1,3]
        random.shuffle(start)
        self.x = start[0]
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False
        
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)######????
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <=paddle_pos[3]:
                return True
        return False


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id) 
        #переменная пос хранит координаты объекта
        #в виде списка из 4 координат [0],[2] - x , [1],[3] - y
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= 400:
            self.hit_bottom == True
            self.y = 0
            self.x = 0
        if self.hit_paddle(pos) == True:
            self.y = -1
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= 500:
            self.x = -1
class Paddle():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(100, 20, 10, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        #не работает движение ракетки
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)#биндим кнопки 
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0) #берём объект созданные в Конструкторе класса Paddle
        pos = self.canvas.coords(self.id) #берём координаты объекта ракетки self.id
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= 500:
            self.x = 0
    
    def turn_left(self, evt):# почему здесьб evt - event -отслеживает событие, нажатие клавиши
        self.x = - 2 #handle pad
    
    def turn_right(self, evt):
        self.x = 2

tk = Tk() #create Tkinter object
tk.title('Арканоид, но не совсем')#Заголовок окна
tk.resizable(0,0) #Неизменяемый размер окна
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness = 0)
canvas.pack()

pad = Paddle(canvas, 'red')
ball = Ball(canvas, pad, 'green')
while True:
    if ball.hit_bottom == False:
        ball.draw()
        pad.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    