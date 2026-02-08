# Programmering med Python
# Veckouppgift 4
# 5 Turtle graphics
# ----------------------------------------------------------------
# https://www.youtube.com/watch?v=p7CiFhiTdvY
#
# Python har ett paket med inbyggda, enkla funktioner för grafik: turtle.
# Tänk dig att du har en robotarm som håller en penna mot ett papper.
# Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
# forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
# backward - gå bakåt
# left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
# dot - sätt ut en prick med en viss storlek
# speed - normal=6, fast=10, maximal=0
#
# Läs mer här: Turtle graphics — Python 3.13.1 documentation
# Kodexempel:
# import turtle as t
#
# # Upprepa 3 gånger
#for x in range(3):
#     t.forward(100)
#     t.left(120)
#
# # Lyft pennan för att flytta utan att rita
# t.penup()
# t.forward(200)
# t.pendown()
# t.dot(10, "red")
# t.color("blue"
# t.forward(50)
#
# # Låt fönstret stanna kvar tills användaren stänger det
# t.mainloop()
#
# 1 Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.
#
# 2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita. Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempel:
# for x in range(5):
#     t.square()
#     t.move_next()
#
# 3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.
# Tips 1: vad händer om man varierar värdet på range?
# Tips 2: 360 grader motsvarar ett helt varv.
# for x in range(7):
#     t.forward(40)
#     t.right(30)
#
# 4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen. Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.
#
#
# Bonusuppgift, lär dig rekursiva funktioner med turtle graphics:
# Python Turtle Meets Fractal Art: A Recursive Journey
# ----------------------------------------------------------------

print("\n----------------------------------------------------------------")
print("Uppgift 4-5-0\n")

print("\n----------------------------------------------------------------")
print("Uppgift 4-5-1\n")
# 1 Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en
# parameter till funktionen.
import turtle as t

def function_square(length):
    for x in range(4):
        t.forward(length)
        t.left(90)

# Varför öppnas inget rit-fönster när jag använder input?
# length = input("Vilken längd ska kvadratens sidor ha? ")
length = 200
function_square(length)


print("\n----------------------------------------------------------------")
print("Uppgift 4-5-2\n")
# 2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger,
# utan att rita. Tanken är att du ska kunna kombinera den med kvadratfunktionen,
# för att rita flera kvadrater.
# Exempel:
# for x in range(5):
#     t.square()
#     t.move_next()

def function_more_squares(qty):
    for x in range(qty):
        t.square = (function_square(100))
        t.penup()
        t.forward(200)
        t.pendown()

qty = 3
function_more_squares(qty)

# t.mainloop()

print("\n----------------------------------------------------------------")
print("Uppgift 4-5-3\n")
# 3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel.
# Använd parametrar i stället för värdena 7, 40 och 30.
# Tips 1: vad händer om man varierar värdet på range?
# Tips 2: 360 grader motsvarar ett helt varv.
# for x in range(7):
#     t.forward(40)
#     t.right(30)

def function_circle(qty, forward, right):
    for x in range(qty):
        t.forward(forward)
        t.right(right)

qty = 360
forward = 1
right = 1
function_circle(qty, forward, right)

print("\n----------------------------------------------------------------")
print("Uppgift 4-5-4\n")
# 4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med
# turtle-modulen. Kombinera dem och försök få bokstäverna att ritas med samma
# storlek, på en rak linje.

print("\n----------------------------------------------------------------")
print("Uppgift 4-5-5\n")
# Bonusuppgift, lär dig rekursiva funktioner med turtle graphics:
# Python Turtle Meets Fractal Art: A Recursive Journey

print("\n----------------------------------------------------------------")
