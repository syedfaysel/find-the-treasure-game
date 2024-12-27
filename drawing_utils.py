
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