import random

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors



def number_to_name(number):    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'Number is not in correct range'
    
    
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'Invalid name choosen'


def rpsls(name): 
    
    player_number = name_to_number(name)
    computer_number = random.randrange(0, 5)
    computer_guess_name = number_to_name(computer_number)
    
    if player_number == None or computer_guess_name == None:        
        return
    
    result = ''
    cal = (player_number - computer_number) % 5
    
    if cal == 0 :
        result = 'Player and computer tie!'
    elif cal > 2:
         result =  'Computer wins!'
    else:
        result = 'Player wins!'


    print "Player chooses " + name
    print "Computer chooses " + computer_guess_name
    print result
    print ""
    

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



