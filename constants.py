# ------------- Global variable declaration ----------
import time

WINDOW_WIDTH=900
WINDOW_HEIGHT=700
LOOP=True
COUNT=0
TEXT=0

MAX_MOVES=19
MAX_TIME=45

PLAYER_X=627  #start position(circle)
PLAYER_Y=277
RADIUS = 22 

TREASURE_X1,TREASURE_Y1,TREASURE_X2, TREASURE_Y2 = 510,310,550,350 # treasure box position)

START_TIME = time.time() 
ELAPSED_TIME = 0
PAUSED = False
PAUSED_TIME=0

RETRY_BUTTON_LOCATION = (20, WINDOW_HEIGHT - 50)
PAUSE_BUTTON_LOCATION = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 50)
EXIT_BUTTON_LOCATION = (WINDOW_WIDTH - 50, WINDOW_HEIGHT - 50)


### ------------- global variables end here ------------------## 