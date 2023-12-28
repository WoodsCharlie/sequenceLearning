import numpy as np

class DiscardBoard():

    def __init__(self):
        self.discarded = np.zeros(52, dtype=np.int8)
        
    def add_to_board(self, discarded_card):
        self.discarded[discarded_card] += 1
        if(self.discarded[discarded_card] > 2):
            raise ValueError('Too many copies of card')
        

    def num_played(self, card_int):
        return self.discarded[card_int]