# Programmering med Python
# Veckouppgift 4
# 4 Pokerhand
# p444_deal_the_cards
# ----------------------------------------------------------------

import random
from itertools import product

# ----------------------------------------------------------------
# Bygger lista med valör 2-14, lista med kortfärgerna, lista som lägger ihop de båda
# Plockar ut angivet antal kort (qty) ur kortleken
# och returnerar en lista med korten (suit och value)
def function_deal_the_cards(qty):
    card_suit_list = ["Hjärter", "Spader", "Klöver", "Ruter"]
    card_value_list = list(range(2, 15))
    deck_of_cards = list(product(card_suit_list, card_value_list))

# Originalhand
    cards = random.sample(deck_of_cards, qty)

# Testhand
#    cards = [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 5), ('Klöver', 3)]
    return cards

# ----------------------------------------------------------------
# Testhänder --------------------------------
# Royal flush
# cards= [('Ruter', 13), ('Ruter', 10), ('Ruter', 12), ('Ruter', 11), ('Ruter', 14)]

# Straight flush
# cards= [('Spader', 7), ('Spader', 5), ('Spader', 4), ('Spader', 8), ('Spader', 6)]

# Four of a kind
# cards= [('Ruter', 11), ('Hjärter', 11), ('Spader', 11), ('Spader', 5), ('Klöver', 11)]

# Full house
# cards= [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 11), ('Klöver', 3)]

# Flush
# cards= [('Klöver', 11), ('Klöver', 3), ('Klöver', 8), ('Klöver', 9), ('Klöver', 5)]

# Straight
# cards= [('Ruter', 7), ('Hjärter', 6), ('Spader', 3), ('Spader', 5), ('Klöver', 4)]

# Three of a kind
# cards= [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 5), ('Klöver', 3)]

# Two pair
# cards= [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 11), ('Klöver', 14)]

# One pair
# cards= [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 8), ('Klöver', 14)]

# ----------------------------------------------------------------
