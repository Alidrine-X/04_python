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
#
# 1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element:
# färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess,
# för enkelhets skull använder vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]
#
# 2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.
#
# 3 Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda på om
# man har ett par, dvs det finns två kort med samma valör.
#
# Fortsätt att lägga till fler kontroller till funktionen.
# Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
# pretty_print_card(["hjärter", 5]) → "hjärter fem"
#
# Lista med pokerhänder.
# Ett par (två lika kort)
# Två par
# Tretal (tre lika)
# Straight (5 kort i följd, t.ex. 7-8-9-10-11)
# Flush / färg (alla kort har samma färg)
# Hus (par och tretal med olika valörer)
# Fyrtal
# Straight flush (5 kort i följd, med samma färg)
# Femtal
# ----------------------------------------------------------------

# 1. Sortera efter första elementet (Färg)
# ----------------------------------------
# Som standard sorterar Python efter det första värdet i varje tuple (index 0).
# hand = [("Spader", 10), ("Hjärter", 14), ("Klöver", 2)]
# sorterad = sorted(hand)
# # Resultat: [('Hjärter', 14), ('Klöver', 2), ('Spader', 10)] (Alfabetiskt)
#
# 2. Sortera efter andra elementet (Valör)
# ----------------------------------------
# För att sortera efter siffran (index 1) använder du ett key-argument med en
# lambda-funktion.
# # x[1] betyder att vi sorterar baserat på valören
# sorterad_valör = sorted(hand, key=lambda x: x[1])
# # Resultat: [('Klöver', 2), ('Spader', 10), ('Hjärter', 14)]
#
# 3. Sortera efter flera kriterier (Färg OCH Valör)
# ----------------------------------------
# Om du vill att korten ska ligga i färgordning, och att varje färg ska vara
# sorterad från lägst till högst, skickar du in båda indexen i din key.
# # Sorterar först på färg (index 0), sedan på värde (index 1)
# sorterad_komplett = sorted(hand, key=lambda x: (x[0], x[1]))

print("\n----------------------------------------------------------------")
print("Uppgift 4-4-4\n")

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
# Dela ut en pokerhand med qty=5 random kort från en kortlek (tuple-lista)
card_hand = function_deal_the_cards(5)

# Dela upp i färg respektive valör
cards_suit = function_open_cards_suit(card_hand)
cards_value = function_open_cards_value(card_hand)

# Kontrollerar hur många av varje färg respektive valör
cards_suit_set = len(set(cards_suit))
cards_value_set = len(set(cards_value))

# Kontrollerar hur många gånger den vanligaste valören förekommer
cards_value_qty = max([cards_value.count(value) for value in set(cards_value)])

# Kolla fyrtal, kåk, triss, tvåpar, par
# cards_value_set == 2 betyder 2 olika valörer på hand
# cards_value_qty == 4 betyder, valören med flest antal har 4 kort
if cards_value_set == 2:                                # Kåk eller fyrtal
    if cards_value_qty == 4:                            # Fyrtal
        print("Du har fyrtal!")
    else:                                               # Kåk
        print("Du har kåk!")
elif cards_value_set == 3:                              # Triss eller tvåpar
    if cards_value_qty == 3:                            # Triss
        print("Du har triss!")
    else:                                               # Tvåpar
        print("Du har tvåpar!")
elif cards_value_set == 4:                              # Par
    print("Du har ett par!")

# Kolla hög färgstege, färgstege, färg
# cards_suit_set == 1 betyder en färg
elif cards_suit_set == 1:
    if cards_value[0] == 10 and cards_value[4] == 14:   # Royal flush (hög färgstege)
        print("Du har hög färgstege!")
    elif cards_value[4] - cards_value[0] == 4:          # Straight flush (färgstege)
        print("Du har färgstege!")
    else:                                               # Flush (Färg)
        print("Du har färg!")
else:
    print("Inget av värde på handen :(")

print("Random card hand", card_hand)

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

print("\n----------------------------------------------------------------")
