# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = None
dealer_hand = None
player_hand = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object

    def __str__(self):
        car = [str(c) for c in self.cards]
        return "[" + ", ".join(car) + "]"

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand
    
    def has_ace(self):
        for card in self.cards:
            if card.get_rank() == 'A':
                return True        
        return False

    def get_value(self):        
        value = sum([VALUES[card.get_rank()] for card in self.cards])
        ace_value = value + 10
        
        if self.has_ace() and ace_value <= 21:           
            return ace_value
        else:
            return value           
   
    def draw(self, canvas, pos):
        xpos = 0	# draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            card.draw(canvas, [pos[0] + xpos, pos[1]])
            xpos += 100
                               
        
# define deck class 
class Deck:
    def __init__(self):		        
        self.cards = [Card(x, y) for x in SUITS for y in RANKS]	# create a Deck object        

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.cards)	# use random.shuffle() to shuffle the deck

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)	# deal a card object from the deck
    
    def __str__(self):
        car = [str(c) for c in self.cards]
        return "[" + ", ".join(car) + "]"	# return a string representing the deck

    def draw(self, canvas, pos):
        xpos = 0	# draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            #card.draw(canvas, [pos[0] + xpos, pos[1]])
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [xpos+ pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            xpos += 10    
    


#define event handlers for buttons
def deal():
    global outcome, in_play, score, deck, dealer_hand, player_hand

    # if game in progress and player hits deal.. player looses a point.
    if in_play: 
        score -= 1
        
    deck = Deck()
    deck.shuffle()
    
    dealer_hand = Hand()
    player_hand = Hand()
    
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    outcome = "Hit or Stand?"
    
    in_play = True
    
    print "Dealer Hand: " + str(dealer_hand) + "   Value: " + str(dealer_hand.get_value())
    print "------------------------------------------"
    print "Player Hand: " + str(player_hand) + "   Value: " + str(player_hand.get_value())
    print "------------------------------------------"
    print ""
    print outcome
    print "------------------------------------------"

def hit():
    global player_hand, outcome, score, in_play, deck
    
    if not in_play:
        return	# replace with your code below
    
    player_hand.add_card(deck.deal_card())
    
    if player_hand.get_value() > 21:
        outcome = "You have busted!"
        score -= 1
        in_play = False
    
    
    print "Player Hand: " + str(player_hand) + "   Value: " + str(player_hand.get_value())
    print "------------------------------------------"
    print ""
    print outcome
    if not in_play:
        print "Score: " + str(score)
    print "------------------------------------------"
   
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer_hand, outcome, score, in_play, deck
    
    if not in_play:
        return
    
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
    
    if player_hand.get_value() > dealer_hand.get_value() or dealer_hand.get_value() > 21 :
        outcome = "You Won!"
        score += 1
        
    else:
        outcome = "You Lost!"
        score -= 1
        
    in_play = False
    
    print "Dealer Hand: " + str(dealer_hand) + "   Value: " + str(dealer_hand.get_value())
    print "------------------------------------------"
    print "Player Hand: " + str(player_hand) + "   Value: " + str(player_hand.get_value())
    print "------------------------------------------"
    print ""
    print outcome    
    print "Score: " + str(score)
    print "------------------------------------------"
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Deck", (25, 30), 18, "NavajoWhite")
    canvas.draw_text("Blackjack", (260, 30), 18, "NavajoWhite")
    deck.draw(canvas, [25, 50])
    canvas.draw_line([0, 175], [600, 175], 2, "DarkSeaGreen")
    
    canvas.draw_text("Dealer", (25, 210), 18, "NavajoWhite")
    dealer_hand.draw(canvas, [25, 250])    
    canvas.draw_line([0, 375], [600, 375], 2, "DarkSeaGreen")
    
    canvas.draw_text("Player", (25, 410), 18, "NavajoWhite")
    canvas.draw_text(outcome, (250, 410), 18, "NavajoWhite")
    canvas.draw_text("Score: " + str(score), (475, 410), 18, "NavajoWhite")
    player_hand.draw(canvas, [25, 450])    
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [25 + CARD_BACK_CENTER[0], 250 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)   
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)



deal()
# get things rolling
frame.start()



# remember to review the gradic rubric

