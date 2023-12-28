class DiscardBoard():

    def __init__(self):
        self.discarded = []
        
    def add_to_board(self, discarded_card):

        self.discarded.append(discarded_card)
        