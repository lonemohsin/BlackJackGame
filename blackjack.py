from shuffleddeck import shuffledDeck
from dealcard import dealCard
from comparehands import comparehands
from total import total
def blackjack():
    deck=shuffledDeck()
    house=[]
    player=[]
    for i in range(2):
        dealCard(deck,player)
        dealCard(deck,house)

    print('House:{:>7}{:>7}'.format(house[0],house[1]))
    print('You:{:>7}{:>7}'.format(player[0],player[1]))

    answer=input('Hit or stand (default: hit): ')

    while answer in {'','h','hit'}:
        card=dealCard(deck,player)
        print('You got:{:>7}'.format(card))
        if total(player)>21:
            print('You went over... You lose.')
            return
        answer=input('Hit or stand (default: hit): ')


    while total(house)<17:
        card=dealCard(deck,house)
        print('House got:{:>7}'.format(card))

        if total(house)>21:
            print('House went over... You win.')
            return
    return comparehands(house,player)

blackjack()