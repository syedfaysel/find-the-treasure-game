
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *


# MidPoint Line Drawing Algorithm
def draw_points(x, y, color = (1, 1, 1), size=2):
   glColor3fv(color)
   glPointSize(size)
   glBegin(GL_POINTS)
   glVertex2f(x,y)
   glEnd()

def to_zone0(zone, x, y):
   if zone == 0: return (x,y)
   elif zone == 1: return (y,x)
   elif zone == 2: return (y,-x)
   elif zone == 3: return (-x,y)
   elif zone == 4: return (-x,-y)
   elif zone == 5: return (-y,-x)
   elif zone == 6: return (-y,x)
   elif zone == 7: return (x,-y)
   else: raise ValueError("Zone must be in [0, 7]")

def to_zoneM(zone, x, y):
   if zone == 0: return (x,y)
   elif zone == 1: return (y,x)
   elif zone == 2: return (-y,x)
   elif zone == 3: return (-x,y)
   elif zone == 4: return (-x,-y)
   elif zone == 5: return (-y,-x)
   elif zone == 6: return (y,-x)
   elif zone == 7: return (x,-y)
   else: raise ValueError("Zone must be in [0, 7]")

def find_zone(x1,y1,x2,y2):
   dx = x2 - x1
   dy = y2 - y1
   if abs(dx) > abs(dy):
       if dx>=0 and dy>=0: return 0
       elif dx>=0 and dy<=0: return 7
       elif dx<=0 and dy>=0: return 3
       elif dx<=0 and dy<=0: return 4
   else :
       if dx>=0 and dy>=0: return 1
       elif dx<=0 and dy>=0: return 2
       elif dx<=0 and dy<=0: return 5
       elif dx>=0 and dy<=0: return 6

def draw_line(x1, y1, x2, y2, color):
   zone = find_zone(x1,y1,x2,y2)
   x1,y1 = to_zone0(zone, x1, y1)
   x2,y2 = to_zone0(zone, x2, y2)
  
   dx = x2 - x1
   dy = y2 - y1
  
   d = 2*dy - dx
   incrE = 2*dy
   incrNE = 2*(dy - dx)

   x = x1
   y = y1
   x0, y0 = to_zoneM(zone, x, y)
  
   draw_points(x0, y0, color)
   while x < x2:
       if d <= 0:
           d = d + incrE
           x = x + 1
       else:
           d = d + incrNE
           x = x + 1
           y = y + 1
       x0, y0 = to_zoneM(zone, x, y)
      
       draw_points(x0, y0, color)


def convert_zone(x, y, zone):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y

def midPointCircleAlgorithm(radius, center_x, center_y, color):
    d = 1 - radius
    x = 0
    y = radius

    while x < y:
        for i in range(8):
            x_, y_ = convert_zone(x, y, i)
            draw_points(x_ + center_x, y_ + center_y, color, 4)

        if d < 0:
            d += 2 * x + 3
            x += 1
        else:
            d += 2 * x - 2 * y + 5
            x += 1
            y -= 1



# ui
def draw_retry_button(x, y, color = (0.0, 0.0, 1.0)):
   draw_line(x, y, x + 20, y - 20, color)
   draw_line(x, y, x + 20, y + 20, color)
   draw_line(x, y, x + 50, y, color)

def draw_pause_button(x, y, color = (1.0, 0.0, 1.0)):
   draw_line(x + 10, y + 20, x + 10, y - 20, color)
   draw_line(x - 10, y + 20, x - 10, y - 20, color)

def draw_play_button(x, y, color = (1.0, 0.0, 1.0)):
   draw_line(x - 10, y + 20, x - 10, y - 20, color)
   draw_line(x - 10, y + 20, x + 10, y, color)
   draw_line(x - 10, y - 20, x + 10, y, color)

def draw_exit(x, y, color = (1.0, 0.0, 0.0)):
   draw_line(x - 20, y + 20, x + 20, y - 20, color)
   draw_line(x - 20, y - 20, x + 20, y + 20, color)

