# Programmering med Python
# Veckouppgift 4
# 1 Läsa och förstå kod - diskutera i grupp
# ----------------------------------------------------------------
# Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE,
# exakt som den står, och kör den.
# Fick du samma resultat som du trodde? Om inte, varför?
# ----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-0\n")

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1a\n")

# Hej skickas med som argument till foo, men funktionen använder sig inte av t
def foo(t):
    print("test")

foo("hej")

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1b\n")

# Funktionen fun1 anropas inte, 5 3 skrivs ut i print
def fun1(x, y):
    return x * y

print(3, 5)

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1c\n")
# print anropar fun1 och skickar med 3 och 5 som argument
# Funktionen beräknar 3 * 5 och skickar tillbaka 15 som skrivs ut

def fun1(x, y):
    return x * y

print(fun1(3, 5))

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1d\n")
# a anropar funktionen fun2,
# som dels anropar fun2 och skickar med x som är 2 som argument
# som beräknar 5 * 2 och returnerar 10
# och dels anropar fun2 och skickar med y som är 3 som argument
# som beräknar 5 * 3 och returnerar 15
# första fun2 skickar med 25 (dvs. 10 + 15)
# som beräknar 5 * 25 och returnerar 125

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1e\n")
# a sätts till 5
# a räknas upp med 2
# print skriver 7 (dvs 5 + 2)
# Funktionen fun3 anropas inte

a = 5
def fun3(a):
    a += 1

a += 2
print(a)

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1f\n")
# a anropar funktionen goo och skickar med argumenten foo och 3
# Funktionen returnerar ett anrop - foo(3)
# Funktionen foo beräknar 2 * 3 * 3 och returnerar 18

def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1g\n")
# Funktionen "isinstance" kan kontrollera en variabels datatyp.
# Vad gör funktionen is_number? Går det att förbättra koden?

# 1g Original-kod
# def is_number(x):
#     if isinstance(x, int):
#         return True
#     elif isinstance(x, float):
#         return True
#     return False

# Funktionen is_number kollar om datatypen är int eller float och
# returnerar då True annars returneras False
# Det går att kolla flera datatyper i samma isinstance
def is_number(x):
    if isinstance(x, (int, float)):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1h\n")
# När funktionsnamnet följt av parenteser () skrivs på den sista raden,
# körs funktionen average_words med listan som indata.
# Ord (item) med längden 5-7 bokstäver/tecken skrivs ut

def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    print(found)    # Rad tillagd för att få se resultatet
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

print("\n----------------------------------------------------------------")
print("Uppgift 4-1-1i\n")
# En uppgift i tre delar:
# Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
# Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
# Rätta felen, så funktionen gör det den ska.

# 1i Original-kod
# def find_min(numbers):
#    counter = 0
#    for item in numbers:
#        if item < counter:
#            counter = item
#    print(f"The smallest item is: {counter}")
#    return counter

# Funktionen skriver ut det minsta värdet i listan (numbers)
# Om listan är tom, skrivs "The list is empty" ut istället
def find_min(numbers):
    if numbers:
        smallest = numbers[0]
        for item in numbers:
            if item < smallest:
                smallest = item
        print(f"The smallest item is: {smallest}")
        return smallest
    else:
        print("The list is empty")
        return None

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

print("\n----------------------------------------------------------------")
