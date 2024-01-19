
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

    