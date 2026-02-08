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
#
# Möjlig vidareutveckling: bygg ett spel som frågar användaren om man
# vill ta ett nytt kort eller stanna. (slumpa ett tal)
# Gör så att datorn kan simulera en motståndare.
# Målet är att vinna över datorn.
# ----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("Uppgift 4-3-0\n")

print("\n----------------------------------------------------------------")
print("Uppgift 4-3-1\n")
# Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa
# att bli större och större. Förr eller senare kommer man förbi 21.
# Skriv en funktion som skriver ut det första talet i talserien som är
# större än 21.

def function_increase(max_number):
    sum_number_series = 0
    counter = 0
    while sum_number_series <= max_number:
        counter += 1
        sum_number_series += counter
    return sum_number_series

max_number = 21
print(function_increase(max_number))

print("\n----------------------------------------------------------------")
print("Uppgift 4-3-2\n")
# Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13.
# (talen i en vanlig kortlek)
# Tips: importera modulen random och använd funktionen randint för att slumpa
# tal. Exempel: card = random.randint(1, 13)

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
print("Uppgift 4-3-3\n")
# Möjlig vidareutveckling: bygg ett spel som frågar användaren om man
# vill ta ett nytt kort eller stanna. (slumpa ett tal)
# Gör så att datorn kan simulera en motståndare.
# Målet är att vinna över datorn.

# Blackjack-regler
#
# Spelarna får alla kort med framsidan uppåt, och givarens första kort är
# med framsidan uppåt och det andra är med framsidan nedåt.
# Målet med spelet är att komma närmare 21 än givaren utan att gå över 21.
# Om en hand går över 21 kallas det en "bust" eller "break" och insatsen är förlorad.
#
# Om både spelare och dealer har 17, 18 eller 19 så vinner dealern,
# har både spelare och dealer 20 eller 21 så blir det lika,
# dvs ingen vinst till spelaren men spelaren blir heller inte av med sin insats.
# Hos kasinon generellt gäller dock att 17, 18, 19, 20 eller 21 innebär "push",
# det vill säga att man behåller sin insats.
#
# Om totalen är 16 eller mindre måste givaren ta ett kort.
# Givaren måste fortsätta ta kort tills totalen är 17 eller mer, då givaren måste stå.
# Om givaren har ett ess, och om det räknas som 11 skulle det totala beloppet bli 17 eller mer
# (men inte över 21), måste givaren räkna esset som 11 och stå.
# Oh ohh, har inte tagit höjd för att ett ess räknas som 1 ELLER 14 här

new_game = True

while new_game:
    new_card = True
    dealer_card = True
    check_result = True

    play_new_game = (input("\nOm du vill spela Black Jack, skriv Y: "))
    if play_new_game != "Y":
        new_game = False
        break
    else:
        player_one = []
        player_one.append(random.randint(1, 13))
        player_one.append(random.randint(1, 13))
        sum_player_hand = 0
        for card in player_one:
            sum_player_hand += card
        print("Du har fått korten", player_one, "med summan", sum_player_hand)

        dealer = []
        dealer.append(random.randint(1, 13))
        dealer.append(random.randint(1, 13))
        print("Givarens första kort är", dealer[0])

        while new_card:
            if sum_player_hand > 21:
                print("Tyvärr, du gick över 21 och förlorade")
                new_card = False
                break
            else:
                next_card = (input("\nVill du ta ett nytt kort Y/N? "))
                if next_card == "Y":
                    player_one.append(random.randint(1, 13))
                    sum_player_hand = 0
                    for card in player_one:
                        sum_player_hand += card
                    print("Du har nu korten", player_one, "med summan", sum_player_hand)
                else:
                    new_card = False
                    sum_dealer_hand = 0
                    for card in dealer:
                        sum_dealer_hand += card
                    print("Givaren har korten", dealer, "med summan", sum_dealer_hand)

                    while check_result:
                        # Om både spelare och dealer har 17, 18 eller 19 så vinner dealern,
                        # har både spelare och dealer 20 eller 21 så blir det lika.
                        if (sum_dealer_hand > 21 or
                            (sum_dealer_hand < sum_player_hand and sum_dealer_hand > 16)):
                            check_result = False
                            print("Du har vunnit!")
                        elif ((sum_dealer_hand > sum_player_hand) or
                              (sum_dealer_hand == sum_player_hand and sum_dealer_hand in (17, 18, 19))):
                            check_result = False
                            print("Givaren vann den här omgången")
                        elif sum_dealer_hand == sum_player_hand and sum_dealer_hand in (20, 21):
                            check_result = False
                            print("Det blev oavgjort den här omgången")
                        elif sum_dealer_hand < 17:
                            while dealer_card:
                                dealer.append(random.randint(1, 13))
                                for card in dealer:
                                    sum_dealer_hand += card
                                print("Givaren har korten", dealer, "med summan", sum_dealer_hand)
                                if sum_dealer_hand >= 17:
                                    dealer_card = False



print("\n----------------------------------------------------------------")
