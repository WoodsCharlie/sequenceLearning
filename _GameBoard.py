import numpy as np
from transformCard import cardToBoard

class GameBoard():

    def __init__(self):
        #Here, a 1 represents a filled in spot by p1, a 2 represents a filled spot by p2
        #and a zero is empty. The 96 indicies are in order of the game board
        #(As in they are arranged as a sequence board would be arranged but flattened) 
        self.boardSpaces = np.zeros((96,3), dtype=int)

        #Here we keep track of what cards can be played in each board space (in a dictionary). 
        #This has somewhat bad space complexity, but since we only have one board per game, 
        #the time complexity is way worth it

        #Order of suits - H, D, C, S
        self.boardToCardDict = {
            0 : 48, #10 of S
            1 : 50, #Q of S
            2 : 51, #K of S
            3 : 39, #A of S
            4 : 14, #2 of D
            5 : 15, # 3 of D
            6 : 16, #4 of D
            7 : 17, # 5 of D

            8 : 47, #9 of S
            9 : 9, #10 of H
            10 : 8, #9 of H
            11 : 7, #8 of H
            12 : 6, #7 of H
            13 : 5, #6 of H
            14 : 4, #5 of H
            15 : 3, #4 of H
            16 : 2, #3 of H
            17 : 18, #6 of D

            18 : 46, #8 of S
            19 : 11, #Q of H
            20 : 19, #7 of D
            21 : 20, #8 of D
            22 : 21, #9 of D
            23 : 22, #10 of D
            24 : 24, #Q of D
            25 : 25, #K of D
            26 : 1, #2 of H
            27 : 19, #7 of D

            28 : 45, #7 of S
            29 : 12, #K of H
            30 : 18, #6 of D
            31 : 27, #2 of C
            32 : 0, #A of H
            33 : 12, #K of H
            34 : 11, #Q of H
            35 : 13, #A of D
            36 : 40, #2 of S
            37 : 20, #8 of D

            38 : 44, #6 of S
            39 : 0, #A of H
            40 : 17, #5 of D
            41 : 28, #3 of C
            42 : 3, #4 of H
            43 : 2, #3 of H
            44 : 9, #10 of H
            45 : 26, #A of C
            46 : 41, #3 of S
            47 : 21, #9 of D

            48 : 43, #5 of S
            49 : 27, #2 of C
            50 : 16, #4 of D
            51 : 29, #4 of C
            52 : 4, #5 of H
            53 : 1, #2 of H
            54 : 8, #9 of H
            55 : 38, #K of C
            56 : 42, #4 of S
            57 : 22, #10 of D

            58 : 42, #4 of S
            59 : 28, #3 of C
            60 : 15, #3 of D
            61 : 30, #5 of C
            62 : 5, #6 of H
            63 : 6, #7 of H
            64 : 7, #8 of H
            65 : 37, #Q of C
            66 : 43, #5 of S
            67 : 24, #Q of D

            68 : 41, #3 of S
            69 : 29, #4 of C
            70 : 14, #2 of D
            71 : 31, #6 of C
            72 : 32, #7 of C
            73 : 33, #8 of C
            74 : 34, #9 of C
            75 : 35, #10 of C
            76 : 44, #6 of S
            77 : 25, #K of D

            78 : 40, #2 of S
            79 : 30, #5 of C
            80 : 39, #A of S
            81 : 51, #K of S
            82 : 50, #Q of S
            83 : 48, #10 of S
            84 : 47, #9 of S
            85 : 46, #8 of S
            86 : 45, #7 of S
            87 : 13, #A of D

            88 : 31, #6 of C
            89 : 32, #7 of C
            90 : 33, #8 of C
            91 : 34, #9 of C
            92 : 35, #10 of C
            93 : 37, #Q of C
            94 : 38, #K of C
            95 : 26, #A of C
        }

        #This one converts any card to the spaces that it can be played. Note - it does not check for jacks
        #Order of suits - H, D, C, S
        self.cardToBoardDict = {
            0 : (32, 39), #A of H
            1 : (26, 53),
            2 : (16, 43),
            3 : (15, 42),
            4 : (14, 52),
            5 : (13, 62),
            6 : (12, 63),
            7 : (11, 64),
            8 : (10, 54),
            9 : (9, 44),
            10 : -1, #Ignore jacks
            11 : (19, 34),
            12 : (29, 33), #K of H

            13 : (35, 87), #A of D
            14 : (4, 70),
            15 : (5, 60),
            16 : (6, 50),
            17 : (7, 40),
            18 : (17, 30),
            19 : (20, 27),
            20 : (21, 37),
            21 : (22, 47),
            22 : (23, 57),
            23 : -1, #Ignore jacks
            24 : (24, 67),
            25 : (25, 77), #K of D

            26 : (45, 95), #A of C
            27 : (31, 49),
            28 : (41, 59),
            29 : (51, 69),
            30 : (61, 79),
            31 : (71, 88),
            32 : (72, 89),
            33 : (73, 90),
            34 : (74, 91),
            35 : (75, 92),
            36 : -1, #Ignore jacks
            37 : (65, 93),
            38 : (55, 94), #K of C

            39 : (3, 80), #A of S
            40 : (36, 78),
            41 : (46, 68),
            42 : (56, 58),
            43 : (48, 66),
            44 : (38, 76),
            45 : (28, 86),
            46 : (18, 85),
            47 : (8, 84),
            48 : (0, 83),
            49 : -1, #Ignore jacks
            50 : (1, 82),
            51 : (2, 81), #K of S
        }


        #Here we keep track of cards that have been played (so we can look them up and whatnot)
        #Values here are either 0, 1, or 2 
        self.cardsPlayed = np.zeros(52, dtype=int)


    #def add_to_board(self, discarded_card):
        #THIS IS NOT CORRECT - PLACEHOLDER ONLY
    #    self.discarded[discarded_card] += 1
    #    if(self.discarded[discarded_card] > 2):
    #        raise ValueError('Too many copies of card')
        

    #def num_played(self, card_int):
    #    return self.cardsPlayed[card_int]

    
    def cardToBoard(self, card):
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
    