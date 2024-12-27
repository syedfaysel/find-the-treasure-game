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
