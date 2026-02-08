# Programmering med Python
# Veckouppgift 4
# 3 Spelet 21
# ----------------------------------------------------------------
# Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa
# att bli större och större. Förr eller senare kommer man förbi 21.
# Skriv en funktion som skriver ut det första talet i talserien som är
# större än 21.
# ----------------------------------------------------------------
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
