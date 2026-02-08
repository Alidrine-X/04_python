# Programmering med Python
# Veckouppgift 4
# 5 Turtle graphics
# ----------------------------------------------------------------
# print("Uppgift 4-5-4\n")
# 4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med
# turtle-modulen. Kombinera dem och försök få bokstäverna att ritas med samma
# storlek, på en rak linje.

import turtle as t

t.title("Skriver PYTHON")
t.shape("turtle")
t.bgcolor("blue")
t.pensize(5)
t.speed(7)

# Turtle object penny
penny = t.Turtle()
penny.color("red")
penny.pensize(5)
penny.shape("turtle")
penny.penup()
penny.right(90)
penny.forward(240)
penny.right(90)

# Flytta till vänster för att få plats med hela ordet
t.penup()
t.backward(500)
t.right(90)
t.pendown()

# Skriv bokstav P
t.forward(200)
t.penup()
t.right(180)
t.forward(200)
t.right(90)
t.pendown()
for x in range(180):
    t.forward(1)
    t.right(1)

# Förbered för nästa bokstav
t.penup()
t.right(90)
t.forward(115)
t.right(90)
t.forward(50)
t.pendown()

# Skriv bokstaven Y
t.right(70)
t.forward(120)
t.left(140)
t.forward(120)
t.penup()
t.left(180)
t.forward(120)
t.left(20)
t.pendown()
t.forward(87)

# Förbered för nästa bokstav
t.penup()
t.left(90)
t.forward(90)
t.left(90)
t.pendown()

# Skriv bokstaven T
t.forward(200)
t.penup()
t.left(90)
t.forward(40)
t.left(180)
t.pendown()
t.forward(80)

# Förbered för nästa bokstav
t.penup()
t.forward(10)
t.right(90)
t.pendown()

# Skriv bokstaven H
t.forward(200)
t.penup()
t.left(180)
t.forward(100)
t.right(90)
t.pendown()
t.forward(65)
t.penup()
t.right(90)
t.forward(100)
t.left(180)
t.pendown()
t.forward(200)

# Förbered för nästa bokstav
t.penup()
t.right(90)
t.forward(40)
t.pendown()

# Skriv bokstav O
for x in range(45):
    t.forward(1)
    t.right(2)
t.forward(143)
for x in range(90):
    t.forward(1)
    t.right(2)
t.forward(143)
for x in range(45):
    t.forward(1)
    t.right(2)

# Förbered för nästa bokstav
t.penup()
t.forward(40)
t.right(90)
t.pendown()

# Skriv bokstaven N
t.forward(200)
t.penup()
t.left(180)
t.forward(200)
t.right(165)
t.pendown()
t.forward(210)
t.left(165)
t.forward(200)

t.hideturtle()

penny.pendown()
penny.speed(9)
penny.forward(550)
penny.left(175)
penny.forward(350)
penny.right(175)
penny.forward(200)

t.mainloop()

# ----------------------------------------------------------------
