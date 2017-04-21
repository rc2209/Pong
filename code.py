# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
y1_in = 160
y1_final = 240
y2_in = 160
y2_final = 240
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH /2 , HEIGHT /2]
    ball_vel = [random.randrange(2,4),random.randrange(2,4)]
    if direction == RIGHT:
        ball_vel[1] = -ball_vel[1]
    elif direction == LEFT:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]# these are vectors stored as lists


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.choice([RIGHT,LEFT]))
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,y1_in,y1_final,y2_in,y2_final,paddle1_vel,paddle2_vel
    
    
            
        
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] == BALL_RADIUS or ball_pos[1] == HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"white","white")
    
    # update paddle's vertical position, keep paddle on the screen
    if y2_in < 3 or y2_final > 400:
            paddle2_vel = -paddle2_vel
    elif y1_in < 3 or y1_final > 400:
            paddle1_vel = -paddle1_vel
    
    y1_in += paddle1_vel
    y1_final += paddle1_vel
    y2_in += paddle2_vel
    y2_final += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0,y1_in], [0,y1_final],[4,y1_in], [4,y1_final]],8,"white","white")
    canvas.draw_polygon([[600,y2_in], [600,y2_final],[600-4,y2_in], [600-4,y2_final]],8,"white","white")
    
    # determine whether paddle and ball collide
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS :
        if ball_pos[1] > y1_in and ball_pos[1] < y1_final:
            ball_vel[0] = ball_vel[0] + 0.1 * ball_vel[0]                       
            ball_vel[0] = -ball_vel[0]
        else:
            spawn_ball(random.choice([LEFT,RIGHT]))
            score2 += 1
        
        
        
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH :
        if ball_pos[1] > y2_in and ball_pos[1] < y2_final:
            ball_vel[0] = ball_vel[0] + 0.1 * ball_vel[0]                       
            ball_vel[0] = -ball_vel[0]            
        else:
            spawn_ball(random.choice([LEFT,RIGHT]))
            score1 += 1
    
    # draw scores
    canvas.draw_text(str(score1),[20,110],70,"White")
    canvas.draw_text(str(score2),[400,110],70,"White")  
def keydown(key):
    global paddle1_vel, paddle2_vel,y1_in,y1_final,y2_in,y2_final
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = +3
            
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -3
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 3
                 

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
def button_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', button_handler,200)


# start frame
new_game()
frame.start()
