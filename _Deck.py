import numpy as np

class Deck:
    """A class of playing cards"""
    def __init__(self):

        deckofcards = np.arange(52)
        
        """Add a second deck by duplicating cards"""
        deckofcards = np.repeat(deckofcards,2)
        np.random.shuffle(deckofcards)

        deck_list = deckofcards.tolist()

        self.deckofcards = deck_list
    

    def draw_card(self):
        return self.deckofcards.pop(0)


    def deal_hand(self):

        """This model assumes a four player game of Squence"""
        """If there are more or less players, change hand size accordingly"""
        
        hand_size = 6
        hand = []

        for i in range(hand_size):
            hand.append(self.deckofcards.pop(0))

        return hand