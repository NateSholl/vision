import blackjack.tools as bj

user = bj.Player('user')
dealer = bj.Player('dealer')
game_on = True

while game_on == True:
    
    gameDeck = bj.Deck()
    gameDeck.shuffleDeck()
    
    # want to play again
    round_on = False
    round_on_input = input('Do you want to play again? y/n')
    if round_on_input == 'y':
        round_on = True
    else:
        print('See you next time!')

    # round start
    while round_on == True:
        
        # deal cards
        user.addCards(gameDeck.dealOne())
        user.addCards(gameDeck.dealOne())
        dealer.addCards(gameDeck.dealOne())
        dealer.addCards(gameDeck.dealOne())

        if user.is_under_21() == False:
            round_on = False
        print('Your cards = ' + user.__str__())
        print('Dealer Cards = ' + dealer.__str__())
        round_on = False

    game_on = False
