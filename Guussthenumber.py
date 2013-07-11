import simplegui
import random
import math


guess_range = 100
gusses_left = 0
secret_number = 0
    

def init():
    global secret_number, gusses_left
    secret_number = random.randrange(0, guess_range)
    gusses_left = math.ceil(math.log(guess_range)/math.log(2))
    
    print ''
    print 'New game. Range is from 0 to '+ str(guess_range)
    print 'Number of remaining gusses is '+ str(gusses_left)
    
    
def range100():
    global guess_range
    guess_range = 100
    init()    
    
def range1000():
    global guess_range
    guess_range = 1000
    init()    
    
def get_input(guess):
    global gusses_left
    
    try:
        guess_int = int(guess)
        
        print 'Guess was '+ guess
        
        if guess_int == secret_number:
            print 'Correct!'
            init()
            return
        elif guess_int < secret_number:
            print 'Higher!'
        else:
            print 'Lower!'
        
        gusses_left = gusses_left - 1
        print 'Number of remaining gusses is {0}'.format(str(gusses_left))
        
        if gusses_left == 0:
            print 'You ran out of gusses. The number was ' + str(secret_number)
            init()
        
    except ValueError:
        return

    
#f = simplegui.create_frame("Number Game", 200, 200)

#f.add_button("range 1 - 100", range100, 200)
#f.add_button("range 1 - 1000", range1000, 200)
#f.add_input("Enter a guess:", get_input, 200)
# start frame

init()
#f.start()


