import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
y1=20*np.sin(x)
y2=x**2*np.cos(x)+0.5
plt.figure(figsize=(8,5),num="1")
plt.plot(x,y1,"r-",label="y1")
plt.plot(x,y2,"g--",label="y2")
plt.legend()



animals=["sheep","duck","chicken","others","cow"]
quantities=[15,28,12,7,10]
colors=["lightgreen","lightblue","yellow","pink","red"]
plt.figure(figsize=(8,5),num="2")
plt.pie(quantities,labels=animals,colors=colors,shadow=True,explode=(0,0,0,0,0.1),autopct="%1.1f%%",startangle=50)
plt.axis("equal")



import random
x=[1,2,3,4,5,6]
dice_rolls=[random.randint(1,6)for i in range(1,102)]
y=[dice_rolls.count(j)for j in range(1,7)]
t1=["1","2","3","4","5","6"]
plt.figure(figsize=(8,5),num="3")
plt.bar(x=x,height=y,tick_label=t1)
plt.title("Number of dice rolls")
plt.show()
