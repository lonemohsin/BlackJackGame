def total(hand):
    values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'1':10,'J':10,'Q':10,'K':10,'A':11}
    result=0
    numAces=0
    for card in hand:
        result+=values[card[0]]
        if card[0]=='A':
            numAces+=1
    while result>21 and numAces>0:
        result-=10
        numAces-=1
    return result
