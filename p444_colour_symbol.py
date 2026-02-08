# Programmering med Python
# Veckouppgift 4
# 4 Pokerhand
# p444_colour_symbol
# ----------------------------------------------------------------
# Översätt kortfärgens text till en symbol
def function_colour_symbol(card_hand):
    # Färgkoder
    RED = "\033[31m"
    BLACK = "\033[97m" # Eller \033[30m för svart om du har vit bakgrund
    RESET = "\033[0m"

    # Översättningstabell med inbyggd färg
    colour_symbol = {
        "Hjärter": f"{RED}♥{RESET}",
        "Ruter":   f"{RED}♦{RESET}",
        "Spader":  f"{BLACK}♠{RESET}",
        "Klöver":  f"{BLACK}♣{RESET}"
    }

    # Skriv ut korten med symbol
    card_hand_colour = []

    for card in card_hand:
        card_hand_colour.append(colour_symbol[card[0]])
        print(f"{colour_symbol[card[0]]} {card[1]}")

# ----------------------------------------------------------------
