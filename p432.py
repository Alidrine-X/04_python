# Programmering med Python
# Veckouppgift 4
# 3 Spelet 21
# ----------------------------------------------------------------
# Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa
# att bli större och större. Förr eller senare kommer man förbi 21.
# Skriv en funktion som skriver ut det första talet i talserien som är
# större än 21.
#
# Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13.
# (talen i en vanlig kortlek)
# Tips: importera modulen random och använd funktionen randint för att slumpa tal.
# Exempel: card = random.randint(1, 13)
# ----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("Uppgift 4-3-2\n")

import random

def function_increase_random(max_number):
    sum_number_series = 0
    card = 0
    while sum_number_series <= max_number:
        card += random.randint(1, 13)
        sum_number_series += card
        print("Card:",card,"sum_number_series:",sum_number_series) # Koll vilka slumptal
    return sum_number_series

max_number = 21
print(function_increase_random(max_number))

print("\n----------------------------------------------------------------")
