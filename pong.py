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
GAME_MESSAGE = "Press Space to Start"
NO_OF_GAMES = 5 # no of points to score to win the game

player1_score = 0
player2_score = 0

ball_x_direction = 1 # initialise the ball direction to move right
ball_y_direction = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

game_in_progress = False
player_win_message = ""

paddle1_up_on = False
paddle1_down_on = False
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]

paddle2_up_on = False
paddle2_down_on = False
paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]

def ball_init(right):
    global ball_pos, ball_vel
    global ball_x_direction, ball_y_direction
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(120, 240), random.randrange(60,180)]# pixcels per second
    
    if right:
        ball_x_direction = 1        
    else:
        ball_x_direction = -1
    ball_y_direction = -1

def ball_handler():
    global ball_pos, ball_vel
    global ball_x_direction, ball_y_direction 
    
    ball_pos[0] += ((ball_vel[0]/100) * ball_x_direction)
    ball_pos[1] += ((ball_vel[1]/100) * ball_y_direction)
    
    if not game_in_progress:
         ball_init(ball_x_direction == 1) #reposition the ball to the middle of canvas
         return
    
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:    
        ball_x_direction *= -1 #change the balls horizontal direction
        ball_pos[0] = PAD_WIDTH + BALL_RADIUS
        if ball_pos[1] >= paddle1_pos[1] - BALL_RADIUS and ball_pos[1] <= paddle1_pos[1] + BALL_RADIUS + PAD_HEIGHT:
            increase_ball_velocity() # increase balls velocity
        else:
           score(False) # player 2 wins a point           
        
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        ball_x_direction *= -1 #change the balls horizontal direction
        ball_pos[0] = WIDTH - PAD_WIDTH - BALL_RADIUS
        if ball_pos[1] >= paddle2_pos[1] - BALL_RADIUS and ball_pos[1] <= paddle2_pos[1] + BALL_RADIUS + PAD_HEIGHT:            
            increase_ball_velocity() # increase balls velocity
        else:
            score(True) # player 1 wins a point            
        
    if ball_pos[1] - BALL_RADIUS <= 0: # if ball hits the top of canvas
        ball_y_direction *= -1 #change the balls vertical direction
        ball_pos[1] = BALL_RADIUS
        
    if ball_pos[1] - BALL_RADIUS >= HEIGHT - BALL_RADIUS * 2 : # is ball hits the bottom of canvas
        ball_y_direction *= -1 #change the balls vertical direction       
        ball_pos[1] = HEIGHT - BALL_RADIUS

        
def score(is_player1_wins): # scoring 
    global player1_score, player2_score, player_win_message, game_in_progress
    if game_in_progress:
        if is_player1_wins:        
            player1_score += 1
        else:
            player2_score += 1
            
    if player1_score >= NO_OF_GAMES:
        game_in_progress = False
        player_win_message = "Player 1 Wins"    
    elif player2_score >= NO_OF_GAMES:
        game_in_progress = False
        player_win_message = "Player 2 Wins"
    else:
        new_serve()     
    

def increase_ball_velocity(): # increases balls velocity by 10% everytime it hits a paddle        
    ball_vel[0] = ball_vel[0] + ball_vel[0] * 0.10
    ball_vel[1] = ball_vel[1] + ball_vel[1] * 0.10        

    
def reset_paddles():# resets paddles
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    paddle1_vel = paddle2_vel = 5 # initialise paddle velocity       
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2 -HALF_PAD_HEIGHT]
    paddle2_pos = [WIDTH-HALF_PAD_WIDTH, HEIGHT/2 -HALF_PAD_HEIGHT]
        
        
def paddle_handler(): # control paddles    
    if paddle1_up_on:
        if  (paddle1_pos[1] - paddle1_vel) <=0:
            paddle1_pos[1] = 0
        else:
            paddle1_pos[1] -= paddle1_vel
    
    if paddle1_down_on:
        if (paddle1_pos[1] + paddle1_vel + PAD_HEIGHT) >= HEIGHT:
            paddle1_pos[1] = HEIGHT - PAD_HEIGHT
        else:
            paddle1_pos[1] += paddle1_vel
            
    if paddle2_up_on:
        if  (paddle2_pos[1] - paddle2_vel) <=0:
            paddle2_pos[1] = 0
        else:
            paddle2_pos[1] -= paddle2_vel
    
    if paddle2_down_on:
        if (paddle2_pos[1] + paddle2_vel + PAD_HEIGHT) >= HEIGHT:
            paddle2_pos[1] = HEIGHT - PAD_HEIGHT
        else:
            paddle2_pos[1] += paddle2_vel    

    
def new_game(): # starts a new game
    global player_win_message, player1_score, player2_score, game_in_progress
    player_win_message  = ""   
    player1_score = 0
    player2_score = 0
    reset_paddles()
    game_in_progress = True
    if not paddle_timer.is_running():        
        paddle_timer.start()        
    
    if not ball_timer.is_running():
        ball_timer.start()
    new_serve()

    
def new_serve(): # new serve
    global game_in_progress
    if not game_in_progress:
        game_in_progress = True
    
    # initialises ball (ball will move towards the winner of last point)
    ball_init(ball_x_direction == 1) 
   

def draw(c):        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line(paddle1_pos, [paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT], PAD_WIDTH, "White" )
    c.draw_line(paddle2_pos, [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], PAD_WIDTH, "White" )
    # update ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    # draw scores
    c.draw_text(str(player1_score), [150, 100], 50, "White")
    c.draw_text(str(player2_score), [425, 100], 50, "White")
    if not game_in_progress:
        c.draw_text(GAME_MESSAGE, [225, 250], 20, "White")
        c.draw_text(player_win_message, [250, 270], 20, "White")
        
        
def keydown(key):
    global paddle1_up_on, paddle1_down_on, paddle2_up_on, paddle2_down_on
    global game_in_progress
    
    if not game_in_progress and key == simplegui.KEY_MAP[ "space" ]:        
        new_game()
    elif key == simplegui.KEY_MAP[ "W" ]:        
        paddle1_up_on = True
    elif key == simplegui.KEY_MAP[ "S" ]:        
        paddle1_down_on = True        
    elif key == simplegui.KEY_MAP[ "up" ]:        
        paddle2_up_on = True               
    elif key == simplegui.KEY_MAP[ "down" ]:
        paddle2_down_on = True
    else:
        return
        
   
def keyup(key):
    global paddle1_up_on, paddle1_down_on, paddle2_up_on, paddle2_down_on
    
    if key == simplegui.KEY_MAP[ "W" ]:        
        paddle1_up_on = False        
    elif key == simplegui.KEY_MAP[ "S" ]:        
        paddle1_down_on = False        
    elif key == simplegui.KEY_MAP[ "up" ]:        
        paddle2_up_on = False               
    elif key == simplegui.KEY_MAP[ "down" ]:
        paddle2_down_on = False    
    else:
        return    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200 )
paddle_timer = simplegui.create_timer(15, paddle_handler)
ball_timer = simplegui.create_timer(10, ball_handler)

# start frame
frame.start()
