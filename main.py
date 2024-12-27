from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
from constants import *
from drawing_utils import *
from game_logic import *



def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"FIND THE TREASURE")
    glClearColor(.9, .9, .9, 1.0)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouseListener)
    glutSpecialFunc(keyboard_special_keys)
    glutTimerFunc(100, update_timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
