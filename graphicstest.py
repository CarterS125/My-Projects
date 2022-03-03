from graphics import* 


def drawCircle():
    windw=GraphWin("a circle",400,400)
   # c = Circle(Point(150,150),100)
    # c.draw(windw)
    c1 = Line(Point(10,10),Point(10,50))
    c2 = Line(Point(10,10),Point(50,10))
    c3 = Line(Point(10,50),Point(50,50))
    c4 = Line(Point(100,20),Point(150,50))
    c5 = Line(Point(100,20),Point(55,50))
    c6 = Line(Point(118,30),Point(83,30))
    c7 = Line(Point(500,50),Point(50,50))
    c8 = Line(Point(160,20),Point(160,50))
    c9 = Line(Point(0,0),Point(0,0))
    c1.draw(windw)
    c2.draw(windw)
    c3.draw(windw)
    c4.draw(windw)
    c5.draw(windw)
    c6.draw(windw)
    c7.draw(windw)
    c8.draw(windw)
    c9.draw(windw)
    windw.getMouse()
    windw.close()
    
import FuncAnimation
import random
import numpy as np
      
x = []
y = []
colors = []
fig = plt.figure(figsize=(7,5))
      
def animation_func(i):
        x.append(random.randint(0,100))
        y.append(random.randint(0,100))
        colors.append(np.random.rand(1))
        area = random.randint(0,30) * random.randint(0,30)
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.scatter(x, y, c = colors, s = area, alpha = 0.5)
      
animation = FuncAnimation(fig, animation_func,interval = 100)

plt.show()    
drawCircle()
    