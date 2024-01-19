
def find_all_valid_actions(player_hand, game_board):

    hand = player_hand.hand

    valid_actions = [None] * 7

    #check if there are any available positions
    for card in hand:

        if (game_board.cardsPlayed[card] > 1):
            pass

        else:
            valid_actions[card].append(game_board.valid_plays(card))

    return valid_actions