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
    
    
