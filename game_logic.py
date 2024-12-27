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
    global TEXT,START_TIME, PAUSED, PAUSED_TIME,LOOP,PLAYER_X,PLAYER_Y, RADIUS, TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2,COUNT

    if key == b' ' and LOOP==True:
        if PAUSED == False:
            PAUSED = True
        else:
            PAUSED_TIME = time.time() - START_TIME - ELAPSED_TIME
            PAUSED = False
    elif key== b'R' or b'r':
            print("Play again")
            TEXT=0
            PAUSED = False 
            LOOP=True
            START_TIME=time.time() 
            PLAYER_X=627 
            PLAYER_Y=277
            RADIUS = 22 
            TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2=510,310,550,350
            COUNT=0
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


# keyboard special key 
def keyboard_special_keys(key, _, __):
    global COUNT,LOOP,PAUSED,TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2,PLAYER_X,PLAYER_Y,RADIUS
    if not PAUSED and LOOP==True and COUNT<MAX_MOVES:
        if key == GLUT_KEY_LEFT:
            if 250<=TREASURE_Y2<=350 and TREASURE_X2==500:
                pass
            elif TREASURE_Y2==400 and TREASURE_X2==600:
                pass
            elif TREASURE_X2==550 and 150<=TREASURE_Y2<=200:
                pass
            elif (TREASURE_X2==700 and TREASURE_Y2==350) or (TREASURE_X2==600 and TREASURE_Y2==300) or (TREASURE_X2==650 and TREASURE_Y2==200) or (TREASURE_X2==750 and TREASURE_Y2==250):
                pass
            elif  (TREASURE_X1-40<PLAYER_X and TREASURE_Y1<PLAYER_Y<TREASURE_Y2) and (((360<PLAYER_Y<400 or 260<PLAYER_Y<300) and PLAYER_X-40<550) or (210<PLAYER_Y<250 and PLAYER_X-40<450) or (160<PLAYER_Y<200 and PLAYER_X-40<600)):
                pass 
            else:
                COUNT+=1
                if TREASURE_X1>PLAYER_X and TREASURE_X1<PLAYER_X+40 and TREASURE_X2<PLAYER_X+80 and TREASURE_Y2>PLAYER_Y>TREASURE_Y1:
                    PLAYER_X-=50
                    draw_filled_circle(PLAYER_X,PLAYER_Y,RADIUS)
                    
                TREASURE_X1 -= 50
                TREASURE_X2 -= 50
                draw_filled_box(TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2)
        elif key == GLUT_KEY_RIGHT: 
            if TREASURE_X2==700 and 350<=TREASURE_Y2<=400:
                pass
            elif TREASURE_X2==750 and 200<=TREASURE_Y2<=300:
                pass
            elif TREASURE_X2==650 and TREASURE_Y2<=150:
                pass
            elif (TREASURE_X2==550 and TREASURE_Y2==200) or (TREASURE_X2==500 and TREASURE_Y2==300) or (TREASURE_X2==600 and TREASURE_Y2==350) or (TREASURE_X2==650 and TREASURE_Y2==250):
                pass
            elif  (TREASURE_X2+40>PLAYER_X and TREASURE_Y1<PLAYER_Y<TREASURE_Y2) and ((310<PLAYER_Y<350 and PLAYER_X+40>610) or (260<PLAYER_Y<300 and PLAYER_X+40>760) or (210<PLAYER_Y<250 and PLAYER_X+40>660) or (110<PLAYER_Y<150 and PLAYER_X+40>660)):
                pass 
            else:
                COUNT+=1
                if TREASURE_X2<PLAYER_X and TREASURE_X1>PLAYER_X-80 and TREASURE_X2>PLAYER_X-40 and TREASURE_Y2>PLAYER_Y>TREASURE_Y1:
                    PLAYER_X+=50
                    draw_filled_circle(PLAYER_X,PLAYER_Y,RADIUS)
                TREASURE_X1 += 50
                TREASURE_X2 += 50
                draw_filled_box(TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2)
        elif key == GLUT_KEY_DOWN:
            if TREASURE_X2==500 and TREASURE_Y2==250:
                pass
            elif 550<=TREASURE_X2<=650 and TREASURE_Y2==150:
                pass
            elif 700<=TREASURE_X2<=750 and TREASURE_Y2==200:
                pass
            elif (TREASURE_X2==650 and TREASURE_Y2==400) or (TREASURE_X2==550 and TREASURE_Y2==350) or (TREASURE_X2==700 and TREASURE_Y2==300) or (TREASURE_X2==600 and TREASURE_Y2==250):
                pass
            elif  (TREASURE_Y1-40<PLAYER_Y and TREASURE_X1<PLAYER_X<TREASURE_X2) and ((460<PLAYER_X<500 and PLAYER_Y-40<200) or (620<PLAYER_X<650 and PLAYER_Y-40<100) or (550<PLAYER_X<600 and PLAYER_Y-40<210) or (650<PLAYER_X<700 and PLAYER_Y-40<250)):
                pass    
            else:
                COUNT+=1
                if TREASURE_Y1>PLAYER_Y and TREASURE_Y1<PLAYER_Y+40<TREASURE_Y2 and TREASURE_X2>PLAYER_X>TREASURE_X1:
                    PLAYER_Y-=50
                    draw_filled_circle(PLAYER_X,PLAYER_Y,RADIUS)
                TREASURE_Y1 -= 50
                TREASURE_Y2 -= 50
                draw_filled_box(TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2)
        elif key == GLUT_KEY_UP:
            if (500<=TREASURE_X2<=550 and TREASURE_Y2==350): 
                pass
            elif  (TREASURE_Y2+40>PLAYER_Y and TREASURE_X1<PLAYER_X<TREASURE_X2) and ((560<PLAYER_X<600 and PLAYER_Y+40>400) or (710<PLAYER_X<750 and PLAYER_Y+40>300) or (610<PLAYER_X<650 and PLAYER_Y+40>300) or (510<PLAYER_X<550 and PLAYER_Y+40>250)):
                pass    
            elif (TREASURE_Y2==400 and 600<=TREASURE_X2<=700):
                pass
            elif (TREASURE_X2==750 and TREASURE_Y2==300):
                pass  
            elif (TREASURE_X2==600 and TREASURE_Y2==150) or (TREASURE_X2==700 and TREASURE_Y2==200) or (TREASURE_X2==650 and TREASURE_Y2==300) or (TREASURE_X2==550 and TREASURE_Y2==250):
                pass
            else:
                COUNT+=1
                if TREASURE_Y2<PLAYER_Y and TREASURE_Y1<PLAYER_Y-40<TREASURE_Y2 and TREASURE_X2>PLAYER_X>TREASURE_X1:
                    PLAYER_Y+=50
                    draw_filled_circle(PLAYER_X,PLAYER_Y,RADIUS)
                TREASURE_Y1 += 50
                TREASURE_Y2 += 50
                draw_filled_box(TREASURE_X1,TREASURE_Y1,TREASURE_X2,TREASURE_Y2)

        glutPostRedisplay()
