import blackjack.tools as bj

user = bj.Player('user')
dealer = bj.Player('dealer')
game_on = True

while game_on == True:
    
    gameDeck = bj.Deck()
    gameDeck.shuffleDeck()
    user.addCards(gameDeck.dealOne())
    user.addCards(gameDeck.dealOne())
    dealer.addCards(gameDeck.dealOne())
    dealer.addCards(gameDeck.dealOne())
    
    # want to play again
    round_on = False
    round_on_input = input('Do you want to play again? y/n')
    if round_on_input == 'y':
        round_on = True
    else:
        print('See you next time!')

    # round start
    while round_on == True:

        stay = False
        while user.is_blackjack() == False and user.is_under_21() == True and stay == False and dealer.is_blackjack() == False:

            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
        
            hitInput = input('Would you like to hit? y/n')

            if hitInput == 'y':
                user.addCards(gameDeck.dealOne())
                print('Your cards = ' + user.__str__())
                print('Dealer Cards = ' + dealer.__str__())
            elif hitInput == 'n':
                stay = True
            else:
                print('Please only input y/n!')
        
        while dealer.is_blackjack() == False and dealer.sumofHand() <= user.sumofHand() and user.is_under_21() == True:
            dealer.addCards(gameDeck.dealOne())
            if dealer.is_under_21 == False:
                break

        if user.is_blackjack() == True:
            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
            print('Blackjack! Player wins!')
            round_on = False
        elif user.is_under_21() == False:
            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
            print('Player Bust!')
            round_on = False
        elif dealer.is_blackjack() == True:
            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
            print('Dealer Blackjack!')
            round_on = False
        elif dealer.is_under_21() == False:
            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
            print('Dealer Bust. Player Wins!')
        elif user.sumofHand() > dealer.sumofHand() and user.is_under_21() == True:
            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
            print('PlayerWins!')
            round_on = False
        elif user.sumofHand() == dealer.sumofHand():
            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
            print('Game Draw')
        else:
            print('Your cards = ' + user.__str__())
            print('Dealer Cards = ' + dealer.__str__())
            print('Dealer Wins')
            round_on = False
        
    game_on = False
