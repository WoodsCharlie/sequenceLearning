
class PlayerHand():

    def __init__(self, initial_hand):
        self.hand = initial_hand[:]


    def remove_card(self, card):

        self.hand.remove(card)


    def add_card(self, card):

        self.hand.append(card)


    def card_exists(self, card):

        """This one can prob be removed - if this function is ever referenced, delete this comment"""
        return (card in self.hand)

    
    def valid_play(self, card):
        #TODO
        """Add implementation"""

        #card is an int between 0 and 51 (inclusive) that represents the deck
        #suit order = ['club', 'diamond', 'heart', 'spade']
        #card order = ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']

        #[0-12], [13-25], [26-38], [39-51]

        """Two eyed jacks are always valid to play (spade + heart)"""
        if (card == 36 or card == 49):
            return True
        
        """If card is a one eyed jack, """
        if (card == 10 or card == 23):
            #MUST check if the other player has a card down
            #for now, just return true
            return True

        #down here, check to see if it is actually valid
        return False