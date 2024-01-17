
def make_move(game_board, discard_board, deck, action, player, player_hand):
    card = action[0]
    position = action[1]
    remove = action[2]

    position_to_play = game_board.cardToBoardDict[card][position]

    if(remove == 0):
        if(game_board.boardSpaces[position_to_play] == 0):
            game_board.boardSpaces[position_to_play] = player
        else:
            raise ValueError('Space is already taken')
        
    else:
        if(game_board.boardSpaces[position_to_play] != 0):
            game_board.boardSpaces[position_to_play] = 0
        else:
            raise ValueError('Space is not yet taken')
        

    discard_board.add_to_board(card)
    player_hand.remove_card(card)
    player_hand.add_card(deck.draw_card)

    return




