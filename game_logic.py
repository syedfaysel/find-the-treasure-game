from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from constants import *
from game_components import *
from drawing_utils import *
import time


def display():
    global TEXT, COUNT ,LOOP,START_TIME, ELAPSED_TIME, PAUSED, PLAYER_X, PLAYER_Y,RADIUS,TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2

    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()    

    for j in range(8):
        
        for i in range(8):
            draw_base(i,j)
            

    for i in range(8):
        for j in range(8):            
            if i==0 and j!=0 and j!=1 and j!=7:
                map(i,j)
                border(i,j)
            elif i==1 and j!=3 and j!=4 and j!=5 and j!=7:
                border(i,j)
                map(i,j)
            elif i==2 and j!=1 and j!=2 and j!=3 and j!=5:
                border(i,j)
                map(i,j)
            elif i==3 and j!=1 and j!=3 and j!=4 and j!=5 and j!=6:
                border(i,j)
                map(i,j)
            elif i==4 and j!=1 and j!=2 and j!=3 and j!=4 and j!=6:
                border(i,j)
                map(i,j)
            elif i==5 and j!=2 and j!=4 and j!=5 and j!=6:
                border(i,j)
                map(i,j)
            elif i==6 and j!=0 and j!=2 and j!=3 and j!=4:
                border(i,j)
                map(i,j)
            elif i==7 and j!=0 and j!=6 and j!=7:
                border(i,j)
                map(i,j)
    goal()
    draw_retry_button(RETRY_BUTTON_LOCATION[0], RETRY_BUTTON_LOCATION[1])
    draw_exit(EXIT_BUTTON_LOCATION[0], EXIT_BUTTON_LOCATION[1])

    # DRAW TIMER ON DISPLAY
    draw_timer(PAUSE_BUTTON_LOCATION[0] - 50, PAUSE_BUTTON_LOCATION[1] - 50, ELAPSED_TIME)

    if not PAUSED:
        draw_pause_button(PAUSE_BUTTON_LOCATION[0], PAUSE_BUTTON_LOCATION[1])
    else:
        draw_play_button(PAUSE_BUTTON_LOCATION[0], PAUSE_BUTTON_LOCATION[1])
    draw_filled_circle(PLAYER_X,PLAYER_Y,RADIUS)
    draw_filled_box(TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2)
    
    if LOOP==True:
        if 510<PLAYER_X<550 and 210<PLAYER_Y<250:
            print("WIN") 
            LOOP=False  
            TEXT=1
            
        # ---- TIMER and GAME OVER LOGIC -----
        if COUNT>=MAX_MOVES  or ELAPSED_TIME>MAX_TIME:
            print("GAME OVER")
            LOOP=False
            TEXT=2

            
    if TEXT!=0:
        text_show(TEXT)
     
        
    glColor3f(0,0,0)
    glRasterPos2f(100, 580)
    t=f"Move Left:{MAX_MOVES-COUNT}"
    for char in t:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
    glutSwapBuffers()




def update_timer(value):
    global LOOP,START_TIME, ELAPSED_TIME, PAUSED, PAUSED_TIME
    if START_TIME is not None and LOOP==True:
        if PAUSED==False:
            ELAPSED_TIME = time.time() - START_TIME - PAUSED_TIME
            
        elif PAUSED==True:
            PAUSED_TIME = time.time() - START_TIME - ELAPSED_TIME
            print("PAUSED_TIME paused time : ", PAUSED_TIME)
        
    glutPostRedisplay()
    glutTimerFunc(100, update_timer, 0)


def keyboard(key, x, y):
    global TEXT,START_TIME, PAUSED,LOOP,PLAYER_X,PLAYER_Y, RADIUS, TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2,COUNT

    if key == b' ' and LOOP==True:
        if not PAUSED:
            PAUSED = True
        else:
            START_TIME = time.time() - PAUSED_TIME
            PAUSED = False
    elif key== b'R' or b'r':
            print("Play again")
            TEXT=0
            PAUSED = False 
            loop=True
            START_TIME=time.time() 
            PLAYER_X=627 
            PLAYER_Y=277
            RADIUS = 22 
            TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2=510,310,550,350
            COUNT=0
            update_timer('v')
            display()
            glutPostRedisplay()

def mouseListener(button, state, x, y):
    global PAUSED_TIME, TEXT, COUNT, LOOP, PAUSED, START_TIME, PLAYER_X, PLAYER_Y, RADIUS, TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if (20< x < 72 and 47 < y < 71):
            print("Play again")
            TEXT=0
            PAUSED = False 
            LOOP=True
            START_TIME=time.time() 
            PAUSED_TIME=0
            PLAYER_X=627 
            PLAYER_Y=277
            RADIUS = 22 
            TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2=510,310,550,350
            COUNT=0
            update_timer('v')
            display()
            glutPostRedisplay()
        elif 438 < x < 461 and 29 < y < 72 and LOOP==True:
            PAUSED = not PAUSED  
            if PAUSED:
                print("Pause")
            else:
                print("Resume")
                
        elif 831 < x < 872 and 33 < y < 70:
            print("Goodbye")
            glutLeaveMainLoop()
  