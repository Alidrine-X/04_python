# Programmering med Python
# Veckouppgift 4
# 2 Öva på funktioner och moduler
# ----------------------------------------------------------------
# Samla ihop dina funktioner så att de ligger i en eller flera moduler.
# Importera och anropa dem från main.py, så att main-filen bara innehåller
# funktionsanrop.
# ----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-0\n")

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-1\n")
# 1 Skriv en funktion som tar en sträng som parameter. När den anropas ska
# den skriva ut strängen och "är en fena på programmering". Exempel:
# my_function("David") → "David är en riktig hacker"

def function_hacker(name):
    print(f" {name} är en riktig hacker")
    return name

function_hacker("Lena")

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-2a\n")
# 2a Skriv en funktion med namnet "eko". När den anropas med en sträng ska den
# upprepa strängen, och skriva ut resultatet.
# Exempel: eko("hej") → skriver ut "hejhej"

def function_echo_two_times(repeat):
    print(repeat + repeat)
    return

function_echo_two_times("hej")

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-2b\n")
# 2b Lägg till en parameter "count", som avgör hur många ekon som ska skapas.
# Exempel: eko("hej", 3) → skriver ut "hejhejhej"

def function_echo(echo_string, echo_times):
#   print(echo_string * echo_times) # Annas version
    echo_result = ""
    for counter in range(echo_times):
        echo_result += echo_string
        counter += 1
    return echo_result

print(function_echo("hej", 5))

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-3\n")
# 3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion
# och justera den enligt kommentaren.

# Original:
# end = 5
# y = 1
# for x in range(1, 100):
#     y *= 2
#     # avsluta loopen med en if-sats här
# print(y)

def function_end(end, y):

    for x in range(1, 100):
        y *= 2  # y=2, y=4, y=8, y=16, y=32

        if x == end: # avsluta loopen med en if-sats här
            return y
    return None # Förslag från PyCharm, ska den vara med?

end = 5
y = 1

print(function_end(end, y))

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-4\n")
# 4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och
# returnera det sista elementet i listan.
# last([1, 2, 3]) → 3
# lista = [1, 2, 3, 4, 5, 6]

def function_last(lista):
    return lista[-1]

lista = [1, 2, 3, 4, 5, 6]
print("Sista elementet i listan är:", function_last(lista))

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-5\n")
# 5 Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter.
# När den anropas ska den returnera en ny lista, där den har tagit bort första
# och sista elementet.
# cut_edges([1, 2, 3, 4]) → [2, 3]

# Slicing används för att plocka ut en specifik del av en lista eller sträng.
# Syntaxen är lista[start:stopp:steg]

def function_cut_edges(cut_lista):
    new_list = cut_lista[4:-2]
    return new_list

cut_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(function_cut_edges(cut_lista))

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-6\n")
# 6 Lös felen i koden.

# Original:
#def increase(x):
#    return x
#    x += 1

#print(increase(1))

def increase(x):
    x += 1
    return x

print(increase(1))

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-7\n")
# 7 Bygg en funktion med namnet average. Den ska ta parametrar: x och y.
# Båda ska vara tal. Funktionen ska returnera medelvärdet. Till exempel
# så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2,
# vilket blir 6.
# Tips: det kan vara enklare att använda fler variabler.

def average(x, y):
    return (x + y) / 2

x = 4
y = 8
print(average(x, y))

print("\n----------------------------------------------------------------")
print("Uppgift 4-2-8\n")
# 8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
# Först ska funktionen tala om ifall listan är tom, eller hur många element
# den har. Sedan ska funktionen skriva ut elementen i en punktlista.
# Exempel:
# pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14

def function_list(pretty_print):
    print("Listan har", len(pretty_print), "element")

    for i, item in enumerate(pretty_print, start=1):
        print(f"{i}. {item}")

pretty_print = ["a", "b", 3.14]
function_list(pretty_print)

print("\n----------------------------------------------------------------")
