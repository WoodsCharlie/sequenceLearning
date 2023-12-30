import numpy as np
from transformCard import cardToBoard

class GameBoard():

    def __init__(self):
        #Here, a 1 represents a filled in spot and a zero is empty. The 96 indicies are in order of the game board
        #(As in they are arranged as a sequence board would be arranged but flattened) 
        self.boardSpaces = np.zeros(96, dtype=int)

        #Here we keep track of cards that have been played (so we can look them up and whatnot)
        #Values here are either 0, 1, or 2 
        self.cardsPlayed = np.zeros(52, dtype=int)


    def checkLocations(self, card):

        """First, translate the card (an int with values [0-51]) into a card"""
        return
    
    def updateBoardSpaces(self, card, replace=-1):
        #This function should only be called after verifying that the card / replace combo is a valid move

        if (replace != -1):
            #This means a one eyed jack has been played and a card is being removed
            #We add the jack to cards played
            self.cardsPlayed[card] = self.cardsPlayed[card] + 1

            #Now we need to update the boardSpaces
            boardSpace = cardToBoard(replace)
            self.boardSpaces[boardSpace] = 0

            return
        
        self.cardsPlayed[card] = self.cardsPlayed[card] + 1
        boardSpace = cardToBoard(card)
        self.boardSpaces[boardSpace] = 1
        return


    def playCard(self, card):

        return
    

