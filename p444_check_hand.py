# Programmering med Python
# Veckouppgift 4
# 4 Pokerhand
# p444_check_hand
# ----------------------------------------------------------------
# Kolla fyrtal, kåk, triss, tvåpar, par
# cards_value_set == 2 betyder 2 olika valörer på hand
# cards_value_qty == 4 betyder, valören med flest antal har 4 kort
# Kolla hög färgstege, färgstege, färg
# cards_suit_set == 1 betyder en färg

def function_check_hand(cards_value_set, cards_value_qty, cards_suit_set, cards_value):
    check_hand = ""
    if cards_value_set == 2:                                # Kåk eller fyrtal
        if cards_value_qty == 4:                            # Fyrtal
            check_hand = "Du har fyrtal!"
        else:                                               # Kåk
            check_hand = "Du har kåk!"
    elif cards_value_set == 3:                              # Triss eller tvåpar
        if cards_value_qty == 3:                            # Triss
            check_hand = "Du har triss!"
        else:                                               # Tvåpar
            check_hand = "Du har tvåpar!"
    elif cards_value_set == 4:                              # Par
        check_hand = "Du har ett par!"
    elif cards_suit_set == 1:
        if cards_value[0] == 10 and cards_value[4] == 14:   # Royal flush (hög färgstege)
            check_hand = "Du har hög färgstege!"
        elif cards_value[4] - cards_value[0] == 4:          # Straight flush (färgstege)
            check_hand = "Du har färgstege!"
        else:                                               # Flush (Färg)
            check_hand = "Du har färg!"
    else:
        check_hand = "Inget av värde på handen tyvärr :("

    return check_hand + "\n"

# ----------------------------------------------------------------
