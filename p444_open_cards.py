# Programmering med Python
# Veckouppgift 4
# 4 Pokerhand
# p444_open_cards
# ----------------------------------------------------------------
# Dela upp korten i två olika listor för färg respektive valör
def function_open_cards_suit(card_hand):
    card_suit = []
    i = 0
    for suit in card_hand:
        card_suit.append(card_hand[i][0])
        i += 1
    card_suit = sorted(card_suit)
    return card_suit

def function_open_cards_value(card_hand):
    card_value = []
    i = 0
    for value in card_hand:
        card_value.append(card_hand[i][1])
        i += 1
    card_value = sorted(card_value)
    return card_value

# ----------------------------------------------------------------

