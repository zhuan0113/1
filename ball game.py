from tkinter import *
import time
import random
class ball:
    def __init__(self,canvas,color,width1,height1,racket):
        self.canvas=canvas
        self.racket=racket
        self.id=canvas.create_oval(0,0,40,40,fill=color)
        self.canvas.move(self.id,width1/2,height1/2)
        starPos=[-3,-2,-1,1,2,3]
        random.shuffle(starPos)
        self.x=starPos[0]
        self.y=-step
        self.notTouchBottom=True
    def hitRacket(self,ballPos):
        racketPos=self.canvas.coords(self.racket.id)
        if ballPos[2]>=racketPos[0] and ballPos[2]<=racketPos[2]:
            if ballPos[3]>=racketPos[1] and ballPos[3] <=racketPos[3]:
                return True
        return False
    def ballMove(self):
        self.canvas.move(self.id,self.x,self.y)
        ballPos=self.canvas.coords(self.id)
        if ballPos[1]<=0:
            self.y=step
        if ballPos[3]>=height1:
            self.y=-step
        if ballPos[0]<=0:
            self.x=step
        if ballPos[2]>=width1:
            self.x=-step
        if self.hitRacket(ballPos)==True:
            self.y=-step
        if ballPos[3]>=height1:
            self.notTouchBottom=False
class racket:
     def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,150,30,fill=color)
        self.canvas.move(self.id,250,500)
        self.x=0
        self.canvas.bind_all("<KeyPress-Right>",self.moveRight)
        self.canvas.bind_all("<KeyPress-Left>",self.moveLeft)
     def racketMove(self):
         self.canvas.move(self.id,self.x,0)
         racketPos=self.canvas.coords(self.id)
         if racketPos[0]<=0:
             self.x=0
         if racketPos[2]>=width1:
             self.x=0
     def moveLeft(self,event):
         self.x=-4
     def moveRight(self,event):
         self.x=4   
width1=700
height1=600
step=5
speed=0.01

tk=Tk()
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=width1,height=height1)
canvas.pack()
tk.update()

racket=racket(canvas,"blue")
ball=ball(canvas,"red",width1,height1,racket)


while ball.notTouchBottom:
    try:
        ball.ballMove()
    except:
        break
    racket.racketMove()
    tk.update()
    time.sleep(speed)
    
    
 
