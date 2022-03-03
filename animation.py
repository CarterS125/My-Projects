import tkinter 
import time 


Windw_width=800
Windw_hieght=600
              
Logo_Start_XPostion = 50
Logo_Start_YPosition = 50

Logo_radius = 30
Logo_Min_Movement = 5
Refresh_sec = 0.01

def create_animation_windw():
    Windw = tkinter.TK()
    Windw.title("Resident Evil Logo")
    
    Windw.geometry(f'{Windw_Width}x{Windw_Hieght}')
    
def creat_animation_canvas():
    canvas = tkinter.Canvas(windw)
    canvas.configure(bg='red')
    canvas.pack(fill="both", expand=True)
    return canvas 

def animate_Logo(Windw, canvas, xinc,yinc):
    logo = canvas.create_oval(Logo_start_XPostion-Logo_Radius, 
                              Logo_Start_YPosition-Ball_Radius,
                              Logo_Start_XPosition+Ball_Radius,
                              Logo_Start_YPosition+Ball_Radius,
                              fill="Purple", outline="Black", width=5)   
    while True: 
        canvas.move(logo,xinc,yinc)
        Windw.update
        time.sleep(Refresh_Sec)
        Logo_Pos = canvas.coords(logo)
        al,bl,ar,br = Logo_pos
        if al < abs(xinc) or ar > Window_Width-abs(xinc):
            xinc = -xinc
            if bl < abs(yinc) or br > Window_Height-abs(yinc):
                yinc = -yinc
      
Animation_Windw = create_animation_windw()
Animation_canvas = create_animation_canvas(Animation_Windw)
animate_logo(Animation_Windw,Animation_canvas, Logo_min_movement, Logo_min_movement)        
                              
                           
    
