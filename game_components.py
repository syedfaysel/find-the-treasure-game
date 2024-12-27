from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from drawing_utils import *


def draw_filled_rect_with_points(x1, y1, x2, y2, color=(0.5, 0.5, 0.5)):
    glColor3fv(color)
    glBegin(GL_POINTS)
    for x in range(int(x1), int(x2) + 1):
        for y in range(int(y1), int(y2) + 1):
            glVertex2f(x, y)
    glEnd()

def border(i, j):
    side_color = (0.7, 0.3, 0.3)
    color = (0.8, 0.0, 0.0)
    x1, y1 = 410 + (i * 50), 60 + (j * 50)
    x2, y2 = 450 + (i * 50), 100 + (j * 50)
    draw_filled_box(x1, y1, x2, y2, color) # TODO:: use CONSTANT VARIABLE

    # Side rectangle 1
    x1, y1 = 405 + (i * 50), 55 + (j * 50)
    x2, y2 = 410 + (i * 50), 100 + (j * 50)
    draw_filled_rect_with_points(x1, y1, x2, y2, color=side_color)

    # Side rectangle 2
    x1, y1 = 405 + (i * 50), 55 + (j * 50)
    x2, y2 = 445 + (i * 50), 60 + (j * 50)
    draw_filled_rect_with_points(x1, y1, x2, y2, color=side_color)

def map(i, j):
    
    x1, y1 = 10 + (i * 40), 25 + (j * 40)
    x2, y2 = 45 + (i * 40), 60 + (j * 40)
    draw_filled_rect_with_points(x1, y1, x2, y2, color=(0.7, 0.3, 0.1)) # TODO:: use CONSTANT VARIABLE

def draw_base(i, j):
    base_color = (0.5, 0.5, 0.5)
    side_color = (0.45, 0.4, 0.4)

    # Base rectangle
    x1, y1 = 410 + (i * 50), 60 + (j * 50)
    x2, y2 = 450 + (i * 50), 100 + (j * 50)
    draw_filled_rect_with_points(x1, y1, x2, y2, color=base_color)

    # Side rectangle 1
    x1, y1 = 405 + (i * 50), 55 + (j * 50)
    x2, y2 = 410 + (i * 50), 100 + (j * 50)
    draw_filled_rect_with_points(x1, y1, x2, y2, color=side_color)

    # Side rectangle 2
    x1, y1 = 405 + (i * 50), 55 + (j * 50)
    x2, y2 = 445 + (i * 50), 60 + (j * 50)
    draw_filled_rect_with_points(x1, y1, x2, y2, color=side_color)

def goal():
    draw_filled_rect_with_points(510, 210, 550, 250, color=(1, 1, 0))  # Yellow box
    draw_filled_circle(187, 202, 18)  # blue circle in goal

def draw_filled_box(x1, y1, x2, y2, color=(0, 1, 0)):
    draw_filled_rect_with_points(x1, y1, x2, y2, color=color)

def draw_filled_circle(center_x, center_y, radius):
    color = (0, 0, 1)
    glColor3fv(color)
    glBegin(GL_POINTS)
    for x in range(center_x - radius, center_x + radius + 1):
        for y in range(center_y - radius, center_y + radius + 1):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                glVertex2f(x, y)
    glEnd()


def draw_timer(x, y, ELAPSED_TIME, color=(0, 0, 0)):
    global PAUSED, LOOP
    if PAUSED:
        text_color = (1, 0, 0)  # Red when PAUSED
    else:
        text_color = (0, 0, 0)  # black when running

    glColor3fv(text_color)
    glRasterPos2f(x-5, y - 10)
    TEXT = f"Timer: {ELAPSED_TIME:.2f}s"

    for char in TEXT:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))  # Changed font style and increased size

def text_show(flag):
    glColor3f(1,0,0)
    glRasterPos2f(350, 500)
    if flag==1:
        TEXT="WINNER!!!"
    elif flag==2:
        TEXT="GAME OVER!!!"
    for char in TEXT:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
