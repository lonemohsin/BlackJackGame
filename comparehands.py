from total import total
def comparehands(house,player):
    houseTotal,playerTotal=total(house),total(player)

    if houseTotal>playerTotal:
        print('You lose.')
    elif playerTotal>houseTotal:
        print('You win')
    elif houseTotal==21 and 2==len(house)<len(player):
        print('You lose.')
    elif playerTotal==21 and 2==len(player)<len(house):
        print('You win.')
    else:
        print('A tie.')
