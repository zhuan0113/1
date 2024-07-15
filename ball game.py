from tkinter import *
import time
import random
# 定義 Ball 類別
class ball:
    def __init__(self,canvas,color,width1,height1,racket):
        self.canvas=canvas
        self.racket=racket
        self.id=canvas.create_oval(0,0,40,40,fill=color)
        self.canvas.move(self.id,width1/2,height1/2)
        starPos=[-3,-2,-1,1,2,3]
        random.shuffle(starPos) # 隨機決定球的初始水平移動方向
        self.x=starPos[0]
        self.y=-step            # 初始垂直移動方向
        self.notTouchBottom=True
        self.score=0
    def hitRacket(self,ballPos):
        racketPos=self.canvas.coords(self.racket.id)
        if ballPos[2]>=racketPos[0] and ballPos[2]<=racketPos[2]:     # 檢查球是否在球拍的水平範圍內
            if ballPos[3]>=racketPos[1] and ballPos[3] <=racketPos[3]: # 檢查球是否在球拍的垂直範圍內
                return True
        return False
    def ballMove(self):
        self.canvas.move(self.id,self.x,self.y)
        ballPos=self.canvas.coords(self.id)
        if ballPos[1]<=0:
            self.y=step          # 碰到上邊界，向下反彈
        if ballPos[3]>=height1:
            self.y=-step         # 碰到下邊界，向上反彈
        if ballPos[0]<=0:
            self.x=step          # 碰到左邊界，向右反彈
        if ballPos[2]>=width1:
            self.x=-step         # 碰到右邊界，向左反彈
        if self.hitRacket(ballPos)==True:
            self.y=-step         # 碰到球拍，向上反彈
            self.score+=1
            score_label.config(text=f"Score: {self.score}")
        if ballPos[3]>=height1:
            self.notTouchBottom=False  # 球碰到下邊界，遊戲結束
# 定義 Racket 類別
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
             self.x=0              # 防止球拍超出左邊界
         if racketPos[2]>=width1:
             self.x=0              # 防止球拍超出右邊界
     def moveLeft(self,event):
         self.x=-4
     def moveRight(self,event):
         self.x=4   
width1=700
height1=600
step=5
speed=0.01

tk=Tk()
tk.wm_attributes("-topmost",1)  # 將窗口置頂
canvas=Canvas(tk,width=width1,height=height1)
canvas.pack()
score_label = Label(tk, text="Score: 0", font=("Helvetica", 16))
score_label.pack()
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
tk.mainloop()    
    
 
