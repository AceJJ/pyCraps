import random

class Dice:
    def roll( self ):
        self.up = random.randint( 1, self.sides )
    
    def __init__( self, sides = 6 ):
        self.sides = sides
        self.up = 1

def start_game():
    class state:
        point = 0
        chips = 1000
        bet = 1001
        passline = 'p'
        rolling = True
        first_die = Dice()
        second_die = Dice()
    
    def scoreRoll( pass_type ):
        state.point = 0

        if ( (pass_type == 'pass' and not state.passline.lower() == 'd') or
             (pass_type == 'dont' and state.passline.lower() == 'd') ):
            state.chips += state.bet
        elif pass_type == 'dont':
            state.chips -= state.bet
        else:
            state.chips -= state.bet

        state.bet = state.chips + 1
            
    
    def follow_up_roll( num_rolled ):
        if num_rolled == 7:
            print( "Seven Out" )
            scoreRoll( 'dont' )
        elif num_rolled == state.point:
            print( "Made Point " + str(state.point) )
            scoreRoll( 'pass' )
        else:
            print( str(num_rolled) )
            
    def come_out_roll( num_rolled ):
        if num_rolled == 2 or num_rolled == 3 or num_rolled == 12:
            print( "Craps" )
            scoreRoll( 'dont' )
        elif num_rolled == 11:
            print( "Eleven Yo" )
            scoreRoll( 'pass' )
        elif num_rolled == 7:
            print( "Seven Winner" )
            scoreRoll( 'pass' )
        else:
            state.point = num_rolled
            print( "New Point " + str( num_rolled ) )

    while state.rolling:
        if state.chips == 0:
            print( "Broke!!" )
            state.rolling = False
            break
        elif state.point == 0:
            state.passline = input( "Any Key - Pass Line, D - Don't Pass Bar " )
            # Only choose Pass/Don't on Come Out Roll (no Come bet)
            while state.bet > state.chips:
                try:
                    state.bet = int( input( "Place your bet (Current Chips: " + str(state.chips) + ") " ) )
                except:
                    state.bet = state.chips + 1

        roll_now = input( "Any key - Roll, Quit - Q " )

        if roll_now.lower() != "q":
            state.first_die.roll()
            state.second_die.roll()
            num_rolled = state.first_die.up + state.second_die.up
            
            if state.point == 0:
                come_out_roll( num_rolled )
            else:
                follow_up_roll( num_rolled )

        else:
            state.rolling = False

start_game()
