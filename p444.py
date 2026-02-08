# Programmering med Python
# Veckouppgift 4
# 4 Pokerhand
# ----------------------------------------------------------------
# När man spelar poker har man en hand med 5 kort, som man hoppas
# ska bli bättre än motståndarnas. Du ska bygga en funktion som kan
# utvärdera en pokerhand och tala om hur bra den är.
# Exempel på körning:
# poker_hand(cards)
# "Du fick ett par med valören: 5"
# ----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("Pokerhand\n")

import p444_deal_the_cards as dtc
import p444_open_cards as oc
import p444_check_hand as ch
import p444_colour_symbol as cs

# ----------------------------------------------------------------
# Dela ut en pokerhand med qty=5 random kort från en kortlek (tuple-lista)
card_hand = dtc.function_deal_the_cards(5)

# Dela upp i färg respektive valör
cards_suit = oc.function_open_cards_suit(card_hand)
cards_value = oc.function_open_cards_value(card_hand)

# Kontrollerar hur många av varje färg respektive valör
cards_suit_set = len(set(cards_suit))
cards_value_set = len(set(cards_value))

# Kontrollerar hur många gånger den vanligaste valören förekommer
cards_value_qty = max([cards_value.count(value) for value in set(cards_value)])

# Kontrollerar vilken pokerhand det blev
print(ch.function_check_hand(
    cards_value_set, cards_value_qty, cards_suit_set, cards_value))

# Visa korten med symboler för färg
cs.function_colour_symbol(card_hand)

print("\n----------------------------------------------------------------")
