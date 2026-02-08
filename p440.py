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
# ----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-0\n")

print("\n----------------------------------------------------------------")
print("Uppgift 4-5-1\n")
# 1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista
# med två element: färg och valör. Färg kan vara: ruter, hjärter, spader
# eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder
# vi talen 2 till 14.
# Exempel på ett kort: ["hjärter", 12]

import random
from itertools import product

# Bygger lista med valör 2-14, lista med kortfärgerna, lista som lägger ihop de båda
# Plockar ut angivet antal kort (qty) ur kortleken
# och returnerar en lista med korten (suit och value)
def function_deal_the_cards(qty):
    card_value_list = list(range(2, 15))
    card_suit_list = ["Hjärter", "Spader", "Klöver", "Ruter"]
    deck_of_cards = list(product(card_suit_list, card_value_list))

    cards = random.sample(deck_of_cards, qty)
    return cards

card_hand = function_deal_the_cards(int(input("Hur många kort vill du ha? ")))

# Dela upp kortet i listan och skriv ut
next_card = card_hand.index(card_hand[1])

# Vi stannar vid näst sista kortet (index - 1)
for i in range(len(card_hand) - 1):
    print("Yttre loop index", card_hand[i])
    print(f"Nästa kort ({card_hand[1]})")


# Jämför valörerna (index 1 i tuplen)
#    if card_1[1] == card_2[1]:
#        print(f"Par hittat! {card_1[0]} och {card_2[0]} har båda {card_1[1]}")
#    elif card_2[1] > card_1[1]:
#        print(f"Nästa kort ({card_2[1]}) är högre än nuvarande ({card_1[1]})")

for suit, value in card_hand:
    print(f"{suit} {value}")

print("Card hand:", card_hand)
print("värde", card_hand[0][1])
print("värde", card_hand[1][1])
print("värde", card_hand[2][1])
print("värde", card_hand[3][1])
print("värde", card_hand[4][1])

print("\n----------------------------------------------------------------")
print("Uppgift 4-5-2\n")
# 2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

# ??
# loop in en loop för att jämföra första kortet i den yttre loopen
# mot de andra i inre loopen (utom första kortet)
# andra kortet i den yttre loopen
# mot de andra i inre loopen



print("\n----------------------------------------------------------------")
print("Uppgift 4-5-3\n")
# 3 Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna
# ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.


print("\n----------------------------------------------------------------")
print("Uppgift 4-5-4\n")
# Fortsätt att lägga till fler kontroller till funktionen.
# Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
# pretty_print_card(["hjärter", 5]) → "hjärter fem"

print("\n----------------------------------------------------------------")
