def dealCard(deck,participant):
    card=deck.pop()
    participant.append(card)
    return card
