from graphics import* 
import tkinter
import time 

def drawLogo():
    windw=GraphWin("Resident Evil Logo",300,300)
    
    x = 0 
    while x <=10:
 
    
        t1_r = Polygon(Point(100,60),Point(120,100),Point(70,90))
        t1_w = Polygon(Point(100,60),Point(120,100),Point(70,90))
        t1_r.setFill('Red')
        t1_w.setFill('White') 
    
        t2_r = Polygon(Point(100,60),Point(120,100),Point(140,60))
        t2_w = Polygon(Point(100,60),Point(120,100),Point(140,60))
        t2_r.setFill('Red')
        t2_w.setFill('White')
                   
                     
        t3_r = Polygon(Point(140,60),Point(120,100),Point(170,90))
        t3_w = Polygon(Point(140,60),Point(120,100),Point(170,90))
        t3_r.setFill('Red')
        t3_w.setFill('White')
        
        t4_r = Polygon(Point(170,90),Point(120,100),Point(170,120))
        t4_w = Polygon(Point(170,90),Point(120,100),Point(170,120))
        t4_r.setFill('Red')
        t4_w.setFill('White')
            
        t5_r = Polygon(Point(170,120),Point(120,100),Point(140,150))
        t5_w = Polygon(Point(170,120),Point(120,100),Point(140,150))
        t5_r.setFill('Red')
        t5_w.setFill('White')
        
        t6_r = Polygon(Point(140,150),Point(120,100),Point(100,150))
        t6_w = Polygon(Point(140,150),Point(120,100),Point(100,150))
        t6_r.setFill('Red')
        t6_w.setFill('White')
        
        t7_r = Polygon(Point(100,150),Point(120,100),Point(70,120))
        t7_w = Polygon(Point(100,150),Point(120,100),Point(70,120))
        t7_r.setFill('Red')
        t7_w.setFill('White')
        
        t8_r = Polygon(Point(70,120),Point(120,100),Point(70,90))
        t8_w = Polygon(Point(70,120),Point(120,100),Point(70,90))
        t8_r.setFill('Red')
        t8_w.setFill('White') 
    
    
        time.sleep(.4)
        t1_r.draw(windw)
        time.sleep(.4)
        t1_w.draw(windw)
    
        time.sleep(.4)
        t2_r.draw(windw)
        time.sleep(.4)
        t2_w.draw(windw)
    
        time.sleep(.4)
        t3_r.draw(windw)
        time.sleep(.4)
        t3_w.draw(windw)
   
        time.sleep(.4)
        t4_r.draw(windw)
        time.sleep(.4)
        t4_w.draw(windw)
    
        time.sleep(.4)
        t5_r.draw(windw)
        time.sleep(.4)
        t5_w.draw(windw)
   
        time.sleep(.4)
        t6_r.draw(windw)
        time.sleep(.4)
        t6_w.draw(windw)
    
        time.sleep(.4)
        t7_r.draw(windw)
        time.sleep(.4)
        t7_w.draw(windw)
  
        time.sleep(.4)
        t8_r.draw(windw)
        time.sleep(.4)
        t8_w.draw(windw)
    
   
    windw.getMouse()    
    windw.close()
    x += 1 
drawLogo()
              

     
                              
                           
    
    